#!/usr/bin/env python3
"""Validate the dual-layer GitHub profile and approved samurai visual system."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
MOTION_HERO = ROOT / "assets/hero/yash-kanadhia-living-product-console-dark-motion.svg"
STATIC_HERO = ROOT / "assets/hero/yash-kanadhia-living-product-console-dark.svg"
MEDIA = (
    ROOT / "assets/profile-media/zeref-media-slot.svg",
    ROOT / "assets/profile-media/perfin-os-media-slot.svg",
    ROOT / "assets/profile-media/for-rent-media-slot.svg",
    ROOT / "assets/profile-media/streamnexus-media-slot.svg",
)
DECISION = ROOT / "docs/decisions/GITHUB_PROFILE_SAMURAI_VISUAL_SYSTEM.md"

LOCKED_COPY = (
    "Yash Kanadhia",
    "Product Designer",
    "Toronto, Ontario, Canada",
    "I design and build systems that connect people to outcomes.",
)

METRICS = (
    "2 Ready to Ship Projects",
    "1 Team Project",
    "5 Certificates",
)

TOOLS = (
    "Figma",
    "Linear",
    "Notion",
    "React",
    "SwiftUI",
    "Firebase",
    "Claude",
    "Codex",
    "GitHub",
)

CERTIFICATIONS = (
    "AI Fluency: Framework & Foundations",
    "Claude Code in Action",
    "Introduction to Claude Cowork",
    "Claude Code 101",
    "Scrum Fundamentals Certified",
)

MARKERS = (
    "<!-- DYNAMIC:WRITING:START -->",
    "<!-- DYNAMIC:WRITING:END -->",
    "<!-- DYNAMIC:SIGNALS:START -->",
    "<!-- DYNAMIC:SIGNALS:END -->",
)

SECTIONS = (
    "## 60-second profile",
    "## Deep evidence",
    "## Evidence map",
    "## How I work",
    "## Current signals",
    "## Selected credentials",
    "## Connect",
)

FORBIDDEN_PUBLIC = (
    "Six Sigma Yellow Belt",
    "visitor count",
    "profile views",
    "GitHub streak",
    "seamless",
)

DRAFT = re.compile(r"\b(?:TODO|TBD)\b|REPLACE_ME|https?://(?:www\.)?example\.com", re.I)
SECRET_PATTERNS = (
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"mongodb(?:\+srv)?://[^\s:@/]+:[^\s@/]+@", re.I),
)
PRIVATE_PATHS = (
    re.compile(r"/Users/[^/\s]+/"),
    re.compile(r"/home/[^/\s]+/"),
    re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+\\"),
)
MD_LINK = re.compile(r"(?<!!)\[[^\]]+\]\((?P<href>[^)\s]+)")
HTML_LINK = re.compile(r"<a\b[^>]*\bhref=[\"'](?P<href>[^\"']+)[\"']", re.I)
HTML_IMG = re.compile(r"<img\b(?P<attrs>[^>]+)>", re.I)
ATTR = re.compile(r"(?P<name>[A-Za-z_:][-A-Za-z0-9_:.]*)\s*=\s*[\"'](?P<value>.*?)[\"']")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.M)


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


def slugify(value: str) -> str:
    value = re.sub(r"<[^>]+>|[`*_~]", "", value).strip().lower()
    value = re.sub(r"[^\w\s-]", "", value)
    return re.sub(r"[\s-]+", "-", value).strip("-")


def links(text: str) -> set[str]:
    found = {m.group("href") for m in MD_LINK.finditer(text)}
    found.update(m.group("href") for m in HTML_LINK.finditer(text))
    return found


def validate_copy(text: str, result: Result) -> None:
    for value in LOCKED_COPY:
        if value not in text:
            result.error(f"Missing locked public copy: {value}")
    for credential in CERTIFICATIONS:
        if text.count(credential) != 1:
            result.error(f"Selected certification must appear exactly once: {credential}")
    for marker in MARKERS:
        if text.count(marker) != 1:
            result.error(f"Dynamic marker must appear exactly once: {marker}")
    for phrase in FORBIDDEN_PUBLIC:
        if phrase.lower() in text.lower():
            result.error(f"Forbidden public copy present: {phrase}")
    result.ok("Locked copy, credentials, dynamic markers, and exclusions checked.")


def validate_structure(text: str, result: Result) -> None:
    position = -1
    for section in SECTIONS:
        current = text.find(section)
        if current == -1:
            result.error(f"Missing README section: {section}")
        elif current <= position:
            result.error(f"README section is out of order: {section}")
        position = max(position, current)

    if text.count("<details>") != 5 or text.count("</details>") != 5:
        result.error("README must contain one static-hero drawer and four evidence drawers.")
    if text.count("<summary><strong>Inspect ") != 4:
        result.error("README must contain four evidence drawer summaries.")
    if '<table role="presentation">' in text:
        result.error("Project-card presentation tables are not allowed.")
    if "```mermaid" in text:
        result.error("Profile-level Mermaid diagrams are not allowed.")

    for name in ("Yash Kanadhia", "Alexis Gorospe", "Sarmad Tariq"):
        if name not in text:
            result.error(f"PerFin team attribution missing: {name}")
    if "This profile does not imply solo ownership." not in text:
        result.error("PerFin solo-ownership guardrail is missing.")

    required_boundaries = (
        "does not connect to bank accounts or process payments",
        "does not claim an App Store release or a deployed production backend",
        "portfolio prototype, not a production OTT platform",
        "Checkout and rental completion are simulated",
    )
    for boundary in required_boundaries:
        if boundary not in text:
            result.error(f"Required public boundary missing: {boundary}")

    motion_text = MOTION_HERO.read_text(encoding="utf-8") if MOTION_HERO.is_file() else ""
    for metric in METRICS:
        if metric not in motion_text:
            result.error(f"Motion hero missing approved metric: {metric}")

    tool_row = "Figma · Linear · Notion · React · SwiftUI · Firebase · Claude · Codex · GitHub"
    if tool_row not in text:
        result.error("README tool order does not match the approved operating rail.")

    if text.find("#### Zeref Memory Engine") > text.find("Inspect PerFin OS"):
        result.error("Zeref must lead the deep-evidence layer.")

    result.ok("Dual-layer structure, ownership, boundaries, metrics, and tool order checked.")


def validate_assets(text: str, result: Result) -> None:
    for asset in (MOTION_HERO, STATIC_HERO, *MEDIA, DECISION):
        if not asset.is_file() or asset.stat().st_size == 0:
            result.error(f"Missing required asset: {asset.relative_to(ROOT)}")

    if text.count("./assets/hero/yash-kanadhia-living-product-console-dark-motion.svg") != 1:
        result.error("README must reference the motion hero once.")
    if text.count("./assets/hero/yash-kanadhia-living-product-console-dark.svg") != 1:
        result.error("README must reference the static hero once.")

    for match in HTML_IMG.finditer(text):
        attrs = {a.group("name").lower(): a.group("value") for a in ATTR.finditer(match.group("attrs"))}
        if not attrs.get("src"):
            result.error("README image has no src.")
        if not attrs.get("alt", "").strip():
            result.error(f"README image has empty alt text: {attrs.get('src', 'unknown')}")

    motion = MOTION_HERO.read_text(encoding="utf-8") if MOTION_HERO.is_file() else ""
    static = STATIC_HERO.read_text(encoding="utf-8") if STATIC_HERO.is_file() else ""
    for value in (*LOCKED_COPY, *METRICS, *TOOLS):
        if value not in motion:
            result.error(f"Motion hero missing approved content: {value}")
        if value not in static:
            result.error(f"Static hero missing approved content: {value}")

    if "prefers-color-scheme: light" not in motion:
        result.error("Motion hero lacks adaptive light mode.")
    if "prefers-reduced-motion: reduce" not in motion:
        result.error("Motion hero lacks reduced-motion handling.")

    result.ok("Hero, media slots, decision memory, and image alternatives checked.")


def validate_links(text: str, result: Result) -> set[str]:
    headings = {slugify(m.group(2)) for m in HEADING.finditer(text)}
    external: set[str] = set()
    for href in links(text):
        if href.startswith("#"):
            if urllib.parse.unquote(href[1:]).lower() not in headings:
                result.error(f"README anchor does not resolve: {href}")
        else:
            parsed = urllib.parse.urlparse(href)
            if parsed.scheme:
                if parsed.scheme != "https":
                    result.error(f"External link must use HTTPS: {href}")
                else:
                    external.add(href)
    result.ok(f"Internal anchors and {len(external)} external URLs checked structurally.")
    return external


def validate_hygiene(text: str, result: Result) -> None:
    if DRAFT.search(text):
        result.error("README contains a draft marker.")
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in {".git", ".venv", "node_modules", "__pycache__"} for part in path.parts):
            continue
        if path.suffix.lower() not in {".md", ".py", ".json", ".yml", ".yaml", ".svg", ".txt"}:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(content):
                result.error(f"Possible secret in {path.relative_to(ROOT)}")
        for pattern in PRIVATE_PATHS:
            if pattern.search(content):
                result.error(f"Private path in {path.relative_to(ROOT)}")
    result.ok("Draft, secret, and private-path scans completed.")


def validate_online(urls: Iterable[str], result: Result) -> None:
    for url in sorted(urls):
        request = urllib.request.Request(url, headers={"User-Agent": "kanadhiayash-profile-validator/3.0"}, method="HEAD")
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                if getattr(response, "status", 200) >= 400:
                    result.warn(f"External link returned HTTP {response.status}: {url}")
        except urllib.error.HTTPError as exc:
            if exc.code in {404, 410}:
                result.error(f"External link unavailable ({exc.code}): {url}")
            else:
                result.warn(f"External link could not be confirmed ({exc.code}): {url}")
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            result.warn(f"External link check inconclusive: {url} ({exc})")
    result.ok("Online links checked; transient failures remain warnings.")


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
    print("Profile dual-layer samurai release validation")
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

    text = README.read_text(encoding="utf-8")
    validate_copy(text, result)
    validate_structure(text, result)
    validate_assets(text, result)
    external = validate_links(text, result)
    validate_hygiene(text, result)
    if args.online:
        validate_online(external, result)
    render(result, args.json)
    return 1 if result.errors else 0


if __name__ == "__main__":
    sys.exit(main())
