#!/usr/bin/env python3
"""Validate the GitHub profile before release.

The validator uses only Python's standard library. Static checks are deterministic.
Optional online checks fail only for definitive 404 or 410 responses; transient
network failures, rate limits, and access restrictions are reported as warnings.
"""

from __future__ import annotations

import argparse
import json
import re
import struct
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

HERO_STEM = "yash-kanadhia-living-product-console-dark"
HERO_PNG = ROOT / "assets" / "hero" / f"{HERO_STEM}.png"
HERO_JPG = ROOT / "assets" / "hero" / f"{HERO_STEM}.jpg"
HERO_SVG = ROOT / "assets" / "hero" / f"{HERO_STEM}.svg"

REQUIRED_LOCAL_ASSETS = (
    HERO_PNG,
    HERO_JPG,
    HERO_SVG,
    ROOT / "assets" / "projects" / "flagship-systems.svg",
    ROOT / "assets" / "projects" / "built-product-proof.svg",
    ROOT / "assets" / "projects" / "product-design-studies.svg",
)

REQUIRED_COPY = (
    "Yash Kanadhia",
    "Product Designer",
    "Toronto, Ontario, Canada",
    "I design and build systems that connect people to outcomes.",
    "2 shipped projects · 1 MADS team project · 5 selected certifications",
    "Figma · React · Swift · Firebase · Claude · Codex",
    "Zeref Memory Engine",
    "PerFin OS",
    "For Rent",
    "StreamNexus",
    "Arthenticate",
    "DriveDeal",
    "MADS final team project",
    "Yash Kanadhia, Alexis Gorospe, and Sarmad Tariq",
)

REQUIRED_CERTIFICATIONS = (
    "AI Fluency: Framework & Foundations",
    "Claude Code in Action",
    "Introduction to Claude Cowork",
    "Claude Code 101",
    "Scrum Fundamentals Certified",
)

FORBIDDEN_HERO_COPY = (
    "AI Product & UX Systems Designer",
    "UX Systems",
    "Product Strategy",
)

FORBIDDEN_PUBLIC_COPY = (
    "Six Sigma Yellow Belt",
    "visitor count",
    "profile views",
    "GitHub streak",
)

DYNAMIC_MARKERS = (
    "<!-- DYNAMIC:WRITING:START -->",
    "<!-- DYNAMIC:WRITING:END -->",
    "<!-- DYNAMIC:SIGNALS:START -->",
    "<!-- DYNAMIC:SIGNALS:END -->",
)

TEXT_EXTENSIONS = {".md", ".py", ".json", ".yml", ".yaml", ".svg", ".txt"}
SKIP_DIRS = {".git", ".venv", "node_modules", "dist", "build", "__pycache__"}

SECRET_PATTERNS = {
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "GitHub personal token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b"),
    "Private key block": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "Credentialed MongoDB URI": re.compile(r"mongodb(?:\+srv)?://[^\s:@/]+:[^\s@/]+@", re.I),
}

PRIVATE_PATH_PATTERNS = {
    "macOS user path": re.compile(r"/Users/[^/\s]+/"),
    "Linux home path": re.compile(r"/home/[^/\s]+/"),
    "Windows user path": re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+\\"),
}

PLACEHOLDER_PATTERNS = {
    "TODO marker": re.compile(r"\bTODO\b", re.I),
    "TBD marker": re.compile(r"\bTBD\b", re.I),
    "replacement marker": re.compile(r"REPLACE(?:_ME| THIS)?", re.I),
    "example domain": re.compile(r"https?://(?:www\.)?example\.com", re.I),
    "bracketed link placeholder": re.compile(r"\[(?:LINK|URL)\]", re.I),
}

HTML_IMG_RE = re.compile(r"<img\b(?P<attrs>[^>]+)>", re.I)
ATTR_RE = re.compile(r"(?P<name>[A-Za-z_:][-A-Za-z0-9_:.]*)\s*=\s*[\"'](?P<value>.*?)[\"']")
MD_IMAGE_RE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<src>[^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\)")
MD_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\((?P<href>[^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\)")
HTML_LINK_RE = re.compile(r"<a\b[^>]*\bhref=[\"'](?P<href>[^\"']+)[\"']", re.I)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.M)

USER_AGENT = "kanadhiayash-profile-release-validator/1.0"


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


def slugify_heading(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"[`*_~]", "", value).strip().lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    value = re.sub(r"[\s-]+", "-", value).strip("-")
    return value


def extract_links(text: str) -> set[str]:
    links = {match.group("href") for match in MD_LINK_RE.finditer(text)}
    links.update(match.group("href") for match in HTML_LINK_RE.finditer(text))
    return links


def extract_images(text: str) -> list[tuple[str, str]]:
    images: list[tuple[str, str]] = []
    for match in HTML_IMG_RE.finditer(text):
        attrs = {m.group("name").lower(): m.group("value") for m in ATTR_RE.finditer(match.group("attrs"))}
        images.append((attrs.get("src", ""), attrs.get("alt", "")))
    for match in MD_IMAGE_RE.finditer(text):
        images.append((match.group("src"), match.group("alt")))
    return images


def local_path_from_ref(reference: str) -> Path | None:
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


def iter_public_text_files() -> Iterable[Path]:
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def validate_locked_copy(text: str, result: Result) -> None:
    for item in REQUIRED_COPY:
        if item not in text:
            result.error(f"Missing locked public copy: {item}")

    for credential in REQUIRED_CERTIFICATIONS:
        if text.count(credential) != 1:
            result.error(f"Selected certification must appear exactly once: {credential}")

    hero_region = "\n".join(text.splitlines()[:40])
    if "<strong>Product Designer</strong>" not in hero_region:
        result.error("Product Designer is not the sole explicit hero title.")
    for phrase in FORBIDDEN_HERO_COPY:
        if phrase.lower() in hero_region.lower():
            result.error(f"Forbidden hero phrase present: {phrase}")
    for phrase in FORBIDDEN_PUBLIC_COPY:
        if phrase.lower() in text.lower():
            result.error(f"Forbidden public profile copy present: {phrase}")

    if "ChatGPT" in hero_region:
        result.error("ChatGPT must not appear in the approved hero tool row.")
    if "./assets/yash-kanadhia-github-banner-8k.png" in text:
        result.error("The superseded banner is still referenced by README.md.")

    for marker in DYNAMIC_MARKERS:
        if text.count(marker) != 1:
            result.error(f"Dynamic marker must appear exactly once: {marker}")

    result.ok("Locked title, positioning, attribution, tools, metrics, and credentials checked.")


def validate_assets(text: str, result: Result) -> None:
    for asset in REQUIRED_LOCAL_ASSETS:
        if not asset.is_file() or asset.stat().st_size == 0:
            result.error(f"Required release asset is missing or empty: {asset.relative_to(ROOT)}")

    images = extract_images(text)
    if not images:
        result.error("README.md contains no images.")

    for src, alt in images:
        if not src:
            result.error("README image has no src attribute.")
            continue
        if not alt.strip():
            result.error(f"README image has empty alt text: {src}")
        local = local_path_from_ref(src)
        if local == Path("/__outside_repository__"):
            result.error(f"README image escapes the repository: {src}")
        elif local is not None and not local.is_file():
            result.error(f"README local image does not exist: {src}")

    hero_ref = f"./assets/hero/{HERO_STEM}.png"
    hero_entries = [(src, alt) for src, alt in images if src == hero_ref]
    if len(hero_entries) != 1:
        result.error(f"README must reference the approved hero PNG exactly once: {hero_ref}")
    else:
        hero_alt = hero_entries[0][1].lower()
        for term in ("yash kanadhia", "product designer", "zeref memory engine", "perfin os", "mads team project"):
            if term not in hero_alt:
                result.error(f"Hero alt text must include: {term}")

    if HERO_PNG.is_file():
        try:
            data = HERO_PNG.read_bytes()
            if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
                raise ValueError("invalid PNG signature or IHDR")
            width, height = struct.unpack(">II", data[16:24])
            ratio = width / height
            if width < 1600 or height < 700:
                result.error(f"Hero PNG is below the minimum 1600x700 size: {width}x{height}")
            if not 2.2 <= ratio <= 2.5:
                result.error(f"Hero PNG aspect ratio is outside the approved wide range: {ratio:.3f}")
            result.ok(f"Hero PNG dimensions checked: {width}x{height}.")
        except (OSError, ValueError, struct.error) as exc:
            result.error(f"Unable to validate hero PNG: {exc}")

    if HERO_JPG.is_file() and not HERO_JPG.read_bytes().startswith(b"\xff\xd8"):
        result.error("Hero JPG does not have a valid JPEG signature.")
    if HERO_SVG.is_file():
        svg = read_text(HERO_SVG)
        if "<svg" not in svg or "role=\"img\"" not in svg:
            result.error("Hero SVG wrapper must contain an SVG root and role=\"img\".")

    result.ok("Local asset paths, image fallbacks, and alt text checked.")


def validate_anchors_and_links(text: str, result: Result) -> set[str]:
    headings = {slugify_heading(match.group(2)) for match in HEADING_RE.finditer(text)}
    external: set[str] = set()

    for href in extract_links(text):
        if href.startswith("#"):
            anchor = urllib.parse.unquote(href[1:]).lower()
            if anchor not in headings:
                result.error(f"README internal anchor does not resolve: {href}")
            continue
        parsed = urllib.parse.urlparse(href)
        if parsed.scheme:
            if parsed.scheme != "https":
                result.error(f"External link must use HTTPS: {href}")
            else:
                external.add(href)
            continue
        local = local_path_from_ref(href)
        if local == Path("/__outside_repository__"):
            result.error(f"README link escapes the repository: {href}")
        elif local is not None and not local.exists():
            result.error(f"README local link does not exist: {href}")

    result.ok(f"Internal anchors and {len(external)} unique external URLs checked structurally.")
    return external


def validate_public_hygiene(text: str, result: Result) -> None:
    for label, pattern in PLACEHOLDER_PATTERNS.items():
        if pattern.search(text):
            result.error(f"README contains {label}.")

    for path in iter_public_text_files():
        try:
            content = read_text(path)
        except UnicodeDecodeError:
            continue
        relative = path.relative_to(ROOT)
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(content):
                result.error(f"Possible {label} in {relative}.")
        for label, pattern in PRIVATE_PATH_PATTERNS.items():
            if pattern.search(content):
                result.error(f"Private {label} in {relative}.")

    result.ok("Placeholder, secret-pattern, and private-path scans completed.")


def check_external_links(urls: Iterable[str], result: Result) -> None:
    for url in sorted(urls):
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT}, method="HEAD")
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                status = getattr(response, "status", 200)
                if status >= 400:
                    result.warn(f"External link returned HTTP {status}: {url}")
        except urllib.error.HTTPError as exc:
            if exc.code in {404, 410}:
                result.error(f"External link is definitively unavailable ({exc.code}): {url}")
            else:
                result.warn(f"External link could not be confirmed ({exc.code}): {url}")
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            result.warn(f"External link check was inconclusive: {url} ({exc})")
    result.ok("Online link verification completed with transient failures treated as warnings.")


def render(result: Result, *, json_output: bool) -> None:
    payload = {
        "release_ready": not result.errors,
        "errors": result.errors,
        "warnings": result.warnings,
        "checks": result.checks,
    }
    if json_output:
        print(json.dumps(payload, indent=2))
        return

    print("Profile release validation")
    print(f"Result: {'PASS' if not result.errors else 'BLOCKED'}")
    for check in result.checks:
        print(f"  OK: {check}")
    for warning in result.warnings:
        print(f"  WARNING: {warning}")
    for error in result.errors:
        print(f"  ERROR: {error}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--online", action="store_true", help="Check external URLs over the network.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args()

    result = Result()
    if not README.is_file():
        result.error("README.md is missing.")
        render(result, json_output=args.json)
        return 1

    text = read_text(README)
    validate_locked_copy(text, result)
    validate_assets(text, result)
    external = validate_anchors_and_links(text, result)
    validate_public_hygiene(text, result)
    if args.online:
        check_external_links(external, result)

    render(result, json_output=args.json)
    return 1 if result.errors else 0


if __name__ == "__main__":
    sys.exit(main())
