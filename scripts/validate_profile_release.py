#!/usr/bin/env python3
"""Validate the GitHub profile before release using only the standard library."""

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
SELF = Path(__file__).resolve()
README = ROOT / "README.md"
HERO_STEM = "yash-kanadhia-living-product-console-dark"
HERO_DIR = ROOT / "assets" / "hero"
HERO_PNG = HERO_DIR / f"{HERO_STEM}.png"
HERO_JPG = HERO_DIR / f"{HERO_STEM}.jpg"
HERO_SVG = HERO_DIR / f"{HERO_STEM}.svg"

REQUIRED_ASSETS = (
    HERO_PNG,
    HERO_JPG,
    HERO_SVG,
    ROOT / "assets/projects/flagship-systems.svg",
    ROOT / "assets/projects/built-product-proof.svg",
    ROOT / "assets/projects/product-design-studies.svg",
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

CERTIFICATIONS = (
    "AI Fluency: Framework & Foundations",
    "Claude Code in Action",
    "Introduction to Claude Cowork",
    "Claude Code 101",
    "Scrum Fundamentals Certified",
)

FORBIDDEN_HERO = (
    "AI Product & UX Systems Designer",
    "UX Systems",
    "Product Strategy",
)

FORBIDDEN_PUBLIC = (
    "Six Sigma Yellow Belt",
    "visitor count",
    "profile views",
    "GitHub streak",
)

MARKERS = (
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
    "private key block": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "credentialed MongoDB URI": re.compile(r"mongodb(?:\+srv)?://[^\s:@/]+:[^\s@/]+@", re.I),
}

PRIVATE_PATHS = {
    "macOS user path": re.compile(r"/Users/[^/\s]+/"),
    "Linux home path": re.compile(r"/home/[^/\s]+/"),
    "Windows user path": re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+\\"),
}

PLACEHOLDERS = {
    "TODO marker": re.compile(r"\bTODO\b", re.I),
    "TBD marker": re.compile(r"\bTBD\b", re.I),
    "replacement marker": re.compile(r"REPLACE(?:_ME| THIS)?", re.I),
    "example domain": re.compile(r"https?://(?:www\.)?example\.com", re.I),
    "bracketed link placeholder": re.compile(r"\[(?:LINK|URL)\]", re.I),
}

HTML_IMG = re.compile(r"<img\b(?P<attrs>[^>]+)>", re.I)
ATTR = re.compile(r"(?P<name>[A-Za-z_:][-A-Za-z0-9_:.]*)\s*=\s*[\"'](?P<value>.*?)[\"']")
MD_IMAGE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<src>[^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\)")
MD_LINK = re.compile(r"(?<!!)\[[^\]]+\]\((?P<href>[^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\)")
HTML_LINK = re.compile(r"<a\b[^>]*\bhref=[\"'](?P<href>[^\"']+)[\"']", re.I)
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.M)
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


def slugify(value: str) -> str:
    value = re.sub(r"<[^>]+>|[`*_~]", "", value).strip().lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    return re.sub(r"[\s-]+", "-", value).strip("-")


def links(text: str) -> set[str]:
    found = {m.group("href") for m in MD_LINK.finditer(text)}
    found.update(m.group("href") for m in HTML_LINK.finditer(text))
    return found


def images(text: str) -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    for match in HTML_IMG.finditer(text):
        attrs = {m.group("name").lower(): m.group("value") for m in ATTR.finditer(match.group("attrs"))}
        found.append((attrs.get("src", ""), attrs.get("alt", "")))
    found.extend((m.group("src"), m.group("alt")) for m in MD_IMAGE.finditer(text))
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


def public_text_files() -> Iterable[Path]:
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.resolve() == SELF:
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def validate_copy(text: str, result: Result) -> None:
    for value in REQUIRED_COPY:
        if value not in text:
            result.error(f"Missing locked public copy: {value}")
    for credential in CERTIFICATIONS:
        if text.count(credential) != 1:
            result.error(f"Selected certification must appear exactly once: {credential}")

    hero = "\n".join(text.splitlines()[:40])
    if "<strong>Product Designer</strong>" not in hero:
        result.error("Product Designer is not the sole explicit hero title.")
    for phrase in FORBIDDEN_HERO:
        if phrase.lower() in hero.lower():
            result.error(f"Forbidden hero phrase present: {phrase}")
    for phrase in FORBIDDEN_PUBLIC:
        if phrase.lower() in text.lower():
            result.error(f"Forbidden public profile copy present: {phrase}")
    if "ChatGPT" in hero:
        result.error("ChatGPT must not appear in the approved hero tool row.")
    if "./assets/yash-kanadhia-github-banner-8k.png" in text:
        result.error("The superseded banner is still referenced by README.md.")
    for marker in MARKERS:
        if text.count(marker) != 1:
            result.error(f"Dynamic marker must appear exactly once: {marker}")
    result.ok("Locked public copy and dynamic markers checked.")


def validate_assets(text: str, result: Result) -> None:
    for asset in REQUIRED_ASSETS:
        if not asset.is_file() or asset.stat().st_size == 0:
            result.error(f"Required release asset is missing or empty: {asset.relative_to(ROOT)}")

    readme_images = images(text)
    if not readme_images:
        result.error("README.md contains no images.")
    for src, alt in readme_images:
        if not src:
            result.error("README image has no src attribute.")
            continue
        if not alt.strip():
            result.error(f"README image has empty alt text: {src}")
        resolved = local_path(src)
        if resolved == Path("/__outside_repository__"):
            result.error(f"README image escapes the repository: {src}")
        elif resolved is not None and not resolved.is_file():
            result.error(f"README local image does not exist: {src}")

    hero_ref = f"./assets/hero/{HERO_STEM}.png"
    hero_entries = [(src, alt) for src, alt in readme_images if src == hero_ref]
    if len(hero_entries) != 1:
        result.error(f"README must reference the approved hero PNG exactly once: {hero_ref}")
    else:
        alt = hero_entries[0][1].lower()
        for term in ("yash kanadhia", "product designer", "zeref memory engine", "perfin os", "mads team project"):
            if term not in alt:
                result.error(f"Hero alt text must include: {term}")

    if HERO_PNG.is_file():
        try:
            data = HERO_PNG.read_bytes()
            if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
                raise ValueError("invalid PNG signature or IHDR")
            width, height = struct.unpack(">II", data[16:24])
            ratio = width / height
            if width < 1600 or height < 700:
                result.error(f"Hero PNG is below 1600x700: {width}x{height}")
            if not 2.2 <= ratio <= 2.5:
                result.error(f"Hero PNG aspect ratio is outside 2.2 to 2.5: {ratio:.3f}")
            result.ok(f"Hero PNG dimensions checked: {width}x{height}.")
        except (OSError, ValueError, struct.error) as exc:
            result.error(f"Unable to validate hero PNG: {exc}")
    if HERO_JPG.is_file() and not HERO_JPG.read_bytes().startswith(b"\xff\xd8"):
        result.error("Hero JPG does not have a valid JPEG signature.")
    if HERO_SVG.is_file():
        svg = read_text(HERO_SVG)
        if "<svg" not in svg or "role=\"img\"" not in svg:
            result.error("Hero SVG wrapper must contain an SVG root and role=\"img\".")
    result.ok("Local assets and image alternatives checked.")


def validate_links(text: str, result: Result) -> set[str]:
    headings = {slugify(m.group(2)) for m in HEADING.finditer(text)}
    external: set[str] = set()
    for href in links(text):
        if href.startswith("#"):
            if urllib.parse.unquote(href[1:]).lower() not in headings:
                result.error(f"README internal anchor does not resolve: {href}")
            continue
        parsed = urllib.parse.urlparse(href)
        if parsed.scheme:
            if parsed.scheme != "https":
                result.error(f"External link must use HTTPS: {href}")
            else:
                external.add(href)
            continue
        resolved = local_path(href)
        if resolved == Path("/__outside_repository__"):
            result.error(f"README link escapes the repository: {href}")
        elif resolved is not None and not resolved.exists():
            result.error(f"README local link does not exist: {href}")
    result.ok(f"Internal anchors and {len(external)} external URLs checked structurally.")
    return external


def validate_hygiene(text: str, result: Result) -> None:
    for label, pattern in PLACEHOLDERS.items():
        if pattern.search(text):
            result.error(f"README contains {label}.")
    for path in public_text_files():
        try:
            content = read_text(path)
        except UnicodeDecodeError:
            continue
        relative = path.relative_to(ROOT)
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(content):
                result.error(f"Possible {label} in {relative}.")
        for label, pattern in PRIVATE_PATHS.items():
            if pattern.search(content):
                result.error(f"Private {label} in {relative}.")
    result.ok("Placeholder, secret-pattern, and private-path scans completed.")


def validate_online(urls: Iterable[str], result: Result) -> None:
    for url in sorted(urls):
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT}, method="HEAD")
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                if getattr(response, "status", 200) >= 400:
                    result.warn(f"External link returned HTTP {response.status}: {url}")
        except urllib.error.HTTPError as exc:
            if exc.code in {404, 410}:
                result.error(f"External link is unavailable ({exc.code}): {url}")
            else:
                result.warn(f"External link could not be confirmed ({exc.code}): {url}")
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            result.warn(f"External link check was inconclusive: {url} ({exc})")
    result.ok("Online links checked; transient failures were treated as warnings.")


def render(result: Result, json_output: bool) -> None:
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
    for value in result.checks:
        print(f"  OK: {value}")
    for value in result.warnings:
        print(f"  WARNING: {value}")
    for value in result.errors:
        print(f"  ERROR: {value}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--online", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    result = Result()
    if not README.is_file():
        result.error("README.md is missing.")
        render(result, args.json)
        return 1

    text = read_text(README)
    validate_copy(text, result)
    validate_assets(text, result)
    external = validate_links(text, result)
    validate_hygiene(text, result)
    if args.online:
        validate_online(external, result)
    render(result, args.json)
    return 1 if result.errors else 0


if __name__ == "__main__":
    sys.exit(main())
