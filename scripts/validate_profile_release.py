#!/usr/bin/env python3
"""Validate the GitHub profile README and Organic AlienTech asset contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
README = ROOT / "README.md"

REQUIRED_ASSETS = (
    "assets/hero/yash-kanadhia-alientech-motion.svg",
    "assets/hero/yash-kanadhia-alientech-static.svg",
    "assets/hero/yash-kanadhia-alientech-preview.gif",
    "assets/motion/zeref-system-flow-motion.svg",
    "assets/motion/zeref-system-flow-static.svg",
    "assets/motion/zeref-system-flow-preview.gif",
    "assets/motion/product-working-model-motion.svg",
    "assets/motion/product-working-model-static.svg",
    "assets/motion/product-working-model-preview.gif",
    "assets/tooling/alientech-tool-constellation-motion.svg",
    "assets/tooling/alientech-tool-constellation-static.svg",
    "assets/tooling/alientech-tool-constellation-preview.gif",
    "assets/social/github-profile-og.png",
    "docs/visual-system/logo-sources.md",
)
LOGOS = ("figma", "linear", "notion", "react", "swiftui", "firebase", "claude", "codex", "github")
PARKED_GIFS = {
    "./assets/profile-media/zeref-product-proof.gif",
    "./assets/profile-media/perfin-os-product-proof.gif",
    "./assets/profile-media/for-rent-product-proof.gif",
    "./assets/profile-media/streamnexus-product-proof.gif",
}
REQUIRED_COPY = (
    "Yash Kanadhia",
    "Product Designer",
    "I design and build systems that connect people to outcomes.",
    "Zeref Memory Engine",
    "PerFin OS",
    "For Rent",
    "StreamNexus",
    "Yash Kanadhia, Alexis Gorospe, and Sarmad Tariq",
    "portfolio prototype, not a production streaming platform",
    "not a hosted AI service, model provider, vector database, autonomous decision-maker, or replacement for human review",
)
CERTIFICATIONS = (
    "AI Fluency: Framework & Foundations",
    "Claude Code in Action",
    "Introduction to Claude Cowork",
    "Claude Code 101",
    "Scrum Fundamentals Certified",
)
SECTION_ORDER = (
    "## Overview",
    "## Selected work",
    "## Flagship system",
    "## Product work",
    "## Capabilities",
    "## Evidence map",
    "## How I work",
    "## Product and delivery stack",
    "## Current signals",
    "## Selected credentials",
    "## Let",
)
FORBIDDEN_PUBLIC = (
    "Six Sigma Yellow Belt",
    "visitor count",
    "profile views",
    "GitHub streak",
)
FORBIDDEN_SVG = ("<script", "javascript:", "<foreignobject", "onload=", "onclick=")
TEXT_EXTENSIONS = {".md", ".py", ".json", ".yml", ".yaml", ".svg", ".txt", ".mjs"}
SKIP_DIRS = {".git", "node_modules", ".venv", "dist", "build", "__pycache__"}
SECRET_PATTERNS = {
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "GitHub personal token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b"),
    "private key block": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "credentialed MongoDB URI": re.compile(r"mongodb(?:\+srv)?://[^\s:@/]+:[^\s@/]+@", re.I),
}
PRIVATE_PATHS = {
    "macOS user path": re.compile(r"/Users/[^/\s]+/"),
    "Linux home path": re.compile(r"/home/[^/\s]+/"),
    "Windows user path": re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+\\"),
}
ALLOWED_PRIVATE_PATH_FILES = {
    Path("organic-alientech-codex-handoff.zip"),
}
HTML_IMG = re.compile(r"<img\b(?P<attrs>[^>]+)>", re.I)
ATTR = re.compile(r"(?P<name>[A-Za-z_:][-A-Za-z0-9_:.]*)\s*=\s*[\"'](?P<value>.*?)[\"']")
MD_IMAGE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<src>[^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\)")
MD_LINK = re.compile(r"(?<!!)\[[^\]]+\]\((?P<href>[^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\)")
HTML_LINK = re.compile(r"<a\b[^>]*\bhref=[\"'](?P<href>[^\"']+)[\"']", re.I)
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.M)
USER_AGENT = "kanadhiayash-organic-alientech-validator/1.0"


@dataclass
class Result:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    checks: list[str] = field(default_factory=list)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def ok(self, message: str) -> None:
        self.checks.append(message)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def slugify(value: str) -> str:
    value = re.sub(r"<[^>]+>|[`*_~]", "", value).strip().lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    return re.sub(r"[\s-]+", "-", value).strip("-")


def links(text: str) -> set[str]:
    found = {match.group("href") for match in MD_LINK.finditer(text)}
    found.update(match.group("href") for match in HTML_LINK.finditer(text))
    return found


def images(text: str) -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    for match in HTML_IMG.finditer(text):
        attrs = {item.group("name").lower(): item.group("value") for item in ATTR.finditer(match.group("attrs"))}
        found.append((attrs.get("src", ""), attrs.get("alt", "")))
    found.extend((match.group("src"), match.group("alt")) for match in MD_IMAGE.finditer(text))
    return found


def local_path(reference: str) -> Path | None:
    parsed = urllib.parse.urlparse(reference)
    if parsed.scheme or parsed.netloc or reference.startswith("#"):
        return None
    clean = urllib.parse.unquote(parsed.path).removeprefix("./")
    candidate = (ROOT / clean).resolve()
    try:
        candidate.relative_to(ROOT.resolve())
    except ValueError:
        return Path("/__outside_repository__")
    return candidate


def public_text_files() -> list[Path]:
    files = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.resolve() == SELF:
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        files.append(path)
    return files


def validate_copy(text: str, result: Result) -> None:
    for value in REQUIRED_COPY:
        if value not in text:
            result.error(f"Missing locked public copy: {value}")
    for credential in CERTIFICATIONS:
        if text.count(credential) != 1:
            result.error(f"Selected certification must appear exactly once: {credential}")
    for phrase in FORBIDDEN_PUBLIC:
        if phrase.lower() in text.lower():
            result.error(f"Forbidden public profile copy present: {phrase}")
    if "ChatGPT" in "\n".join(text.splitlines()[:80]):
        result.error("ChatGPT must not appear in the approved hero or top navigation.")
    result.ok("Locked profile copy, credentials, and public exclusions checked.")


def validate_structure(text: str, result: Result) -> None:
    position = -1
    for section in SECTION_ORDER:
        current = text.find(section)
        if current == -1:
            result.error(f"Missing README section: {section}")
            continue
        if current <= position:
            result.error(f"README section is out of order: {section}")
        position = current
    for anchor in ("overview", "selected-work", "capabilities", "evidence-map", "how-i-work", "product-and-delivery-stack", "current-signals", "connect"):
        if f'href="#{anchor}"' not in text and f"id=\"{anchor}\"" not in text:
            result.error(f"Expected navigation or anchor is missing: {anchor}")
    if text.count("<details>") != 5 or text.count("</details>") != 5:
        result.error("README must contain one static-banner drawer and four evidence drawers.")
    if text.count("<summary><strong>Inspect ") != 4:
        result.error("README must provide exactly four evidence-drawer summaries.")
    if '<table role="presentation">' in text or "```mermaid" in text:
        result.error("README must not restore project-card tables or Mermaid diagrams.")
    result.ok("README order, anchors, drawers, and excluded layout patterns checked.")


def validate_svg(path: Path, result: Result, *, motion: bool = False) -> None:
    try:
        ET.parse(path)
    except ET.ParseError as exc:
        result.error(f"SVG does not parse: {path.relative_to(ROOT)} ({exc})")
        return
    svg = read_text(path).lower()
    if "<svg" not in svg or 'role="img"' not in svg or "viewbox=" not in svg:
        result.error(f"SVG must include svg root, viewBox, and role=img: {path.relative_to(ROOT)}")
    if "<title" not in svg or "<desc" not in svg:
        result.error(f"SVG must include title and desc: {path.relative_to(ROOT)}")
    for token in FORBIDDEN_SVG:
        if token in svg:
            result.error(f"Unsafe SVG token {token}: {path.relative_to(ROOT)}")
    if motion and "prefers-reduced-motion" not in svg:
        result.error(f"Motion SVG lacks reduced-motion handling: {path.relative_to(ROOT)}")


def validate_assets(text: str, result: Result) -> None:
    all_required = list(REQUIRED_ASSETS) + [f"assets/tooling/logos/{name}.svg" for name in LOGOS]
    for file in all_required:
        path = ROOT / file
        if not path.is_file() or path.stat().st_size == 0:
            result.error(f"Required asset is missing or empty: {file}")
        elif path.suffix == ".svg":
            validate_svg(path, result, motion=file.endswith("-motion.svg"))
    for src, alt in images(text):
        if not alt.strip():
            result.error(f"README image has empty alt text: {src}")
        if src in PARKED_GIFS:
            continue
        candidate = local_path(src)
        if candidate == Path("/__outside_repository__"):
            result.error(f"README image escapes the repository: {src}")
        elif candidate and not candidate.exists():
            result.error(f"README local image does not exist: {src}")
    logo_doc = ROOT / "docs/visual-system/logo-sources.md"
    if logo_doc.is_file():
        logo_text = read_text(logo_doc)
        for logo in ("Figma", "Linear", "Notion", "React", "SwiftUI", "Firebase", "Claude", "Codex", "GitHub"):
            if f"| {logo} |" not in logo_text:
                result.error(f"Logo source record missing: {logo}")
    result.ok("Required assets, README images, SVG safety, and logo source records checked.")


def validate_links(text: str, result: Result) -> set[str]:
    external: set[str] = set()
    anchors = {slugify(match.group(2)) for match in HEADING.finditer(text)}
    anchors.update(re.findall(r'<a\s+id=["\']([^"\']+)["\']', text, flags=re.I))
    for href in links(text):
        parsed = urllib.parse.urlparse(href)
        if parsed.scheme or parsed.netloc:
            if parsed.scheme != "https":
                result.error(f"External link must use HTTPS: {href}")
            external.add(href)
            continue
        if href.startswith("#"):
            if href[1:] not in anchors:
                result.error(f"README internal anchor does not resolve: {href}")
            continue
        candidate = local_path(href)
        if candidate == Path("/__outside_repository__"):
            result.error(f"README link escapes the repository: {href}")
        elif candidate and not candidate.exists():
            result.error(f"README local link does not exist: {href}")
    result.ok(f"Internal anchors and {len(external)} external URLs checked structurally.")
    return external


def scan_public_files(result: Result) -> None:
    for path in public_text_files():
        rel = path.relative_to(ROOT)
        if rel in ALLOWED_PRIVATE_PATH_FILES:
            continue
        text = read_text(path)
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                result.error(f"{label} detected in {rel}")
        for label, pattern in PRIVATE_PATHS.items():
            if pattern.search(text):
                result.error(f"{label} detected in {rel}")
    result.ok("Secret and private-path scans completed.")


def validate_online_links(urls: set[str], result: Result) -> None:
    for url in sorted(urls):
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                if response.status in {404, 410}:
                    result.error(f"External link is unavailable ({response.status}): {url}")
                elif response.status >= 400:
                    result.warn(f"External link returned HTTP {response.status}: {url}")
        except urllib.error.HTTPError as exc:
            if exc.code in {404, 410}:
                result.error(f"External link is unavailable ({exc.code}): {url}")
            else:
                result.warn(f"External link could not be confirmed ({exc.code}): {url}")
        except Exception as exc:
            result.warn(f"External link check was inconclusive: {url} ({exc})")
    result.ok("Online links checked; transient failures were treated as warnings.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--online", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    result = Result()
    if not README.is_file():
        result.error("README.md is missing.")
        text = ""
    else:
        text = read_text(README)
        validate_copy(text, result)
        validate_structure(text, result)
        validate_assets(text, result)
        external = validate_links(text, result)
        scan_public_files(result)
        if args.online:
            validate_online_links(external, result)

    if args.json:
        print(json.dumps({"errors": result.errors, "warnings": result.warnings, "checks": result.checks}, indent=2))
    else:
        print("Organic AlienTech profile release validation")
        print(f"Result: {'BLOCKED' if result.errors else 'PASS'}")
        for check in result.checks:
            print(f"  OK: {check}")
        for warning in result.warnings:
            print(f"  WARNING: {warning}")
        for error in result.errors:
            print(f"  ERROR: {error}")
    return 1 if result.errors else 0


if __name__ == "__main__":
    sys.exit(main())
