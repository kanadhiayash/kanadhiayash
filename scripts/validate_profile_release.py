#!/usr/bin/env python3
"""Validate the locked dual-layer GitHub profile and three-layer theme system."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
MOTION = ROOT / "assets/hero/yash-kanadhia-living-product-console-dark-motion.svg"
STATIC = ROOT / "assets/hero/yash-kanadhia-living-product-console-dark.svg"
DECISION = ROOT / "docs/decisions/GITHUB_PROFILE_SAMURAI_VISUAL_SYSTEM.md"
MEDIA = tuple(ROOT / f"assets/profile-media/{name}-media-slot.svg" for name in (
    "zeref", "perfin-os", "for-rent", "streamnexus"
))
PORTALS = tuple(ROOT / path for path in (
    "assets/navigation/metric-ready-to-ship.svg",
    "assets/navigation/metric-team-project.svg",
    "assets/navigation/metric-certificates.svg",
    "assets/evidence/zeref-alientech-portal.svg",
))

LOCKED = (
    "Yash Kanadhia",
    "Product Designer",
    "Toronto, Ontario, Canada",
    "I design and build systems that connect people to outcomes.",
)
METRICS = ("2 Ready to Ship Projects", "1 Team Project", "5 Certificates")
TOOLS = ("Figma", "Linear", "Notion", "React", "SwiftUI", "Firebase", "Claude", "Codex", "GitHub")
TOOL_ROW = "Figma · Linear · Notion · React · SwiftUI · Firebase · Claude · Codex · GitHub"
CERTS = (
    "AI Fluency: Framework & Foundations",
    "Claude Code in Action",
    "Introduction to Claude Cowork",
    "Claude Code 101",
    "Scrum Fundamentals Certified",
)
SECTIONS = (
    "## 60-second profile", "## Deep evidence", "## Evidence map",
    "## How I work", "## Current signals", "## Selected credentials", "## Connect",
)
MARKERS = (
    "<!-- DYNAMIC:WRITING:START -->", "<!-- DYNAMIC:WRITING:END -->",
    "<!-- DYNAMIC:SIGNALS:START -->", "<!-- DYNAMIC:SIGNALS:END -->",
)
FORBIDDEN = ("Six Sigma Yellow Belt", "visitor count", "profile views", "GitHub streak", "seamless")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.M)
EXPLICIT_ID = re.compile(r"\bid=[\"']([^\"']+)[\"']", re.I)
LINK = re.compile(r"(?:href=[\"']|\]\()(?P<href>#[^\"')\s]+|https://[^\"')\s]+)")
IMG = re.compile(r"<img\b(?P<attrs>[^>]+)>", re.I)
ATTR = re.compile(r"(?P<name>[A-Za-z_:][-A-Za-z0-9_:.]*)\s*=\s*[\"'](?P<value>.*?)[\"']")
SECRET = (
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"mongodb(?:\+srv)?://[^\s:@/]+:[^\s@/]+@", re.I),
)
PRIVATE = (
    re.compile(r"/Users/[^/\s]+/"),
    re.compile(r"/home/[^/\s]+/"),
    re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+\\"),
)


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


def slug(value: str) -> str:
    value = re.sub(r"<[^>]+>|[`*_~]", "", value).strip().lower()
    value = re.sub(r"[^\w\s-]", "", value)
    return re.sub(r"[\s-]+", "-", value).strip("-")


def validate_svg(path: Path, result: Result) -> str:
    if not path.is_file() or path.stat().st_size == 0:
        result.error(f"Missing required asset: {path.relative_to(ROOT)}")
        return ""
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    for token in ("<svg", 'role="img"', "<title", "<desc"):
        if token not in lower:
            result.error(f"SVG accessibility contract missing {token}: {path.relative_to(ROOT)}")
    for token in ("<script", "javascript:", "onload=", "onclick=", "<foreignobject"):
        if token in lower:
            result.error(f"Unsafe SVG token {token}: {path.relative_to(ROOT)}")
    return text


def validate(text: str, result: Result) -> None:
    for item in LOCKED:
        if item not in text:
            result.error(f"Missing locked copy: {item}")
    for item in CERTS:
        if text.count(item) != 1:
            result.error(f"Credential must appear once: {item}")
    for item in MARKERS:
        if text.count(item) != 1:
            result.error(f"Dynamic marker must appear once: {item}")
    for item in FORBIDDEN:
        if item.lower() in text.lower():
            result.error(f"Forbidden public copy: {item}")

    position = -1
    for section in SECTIONS:
        current = text.find(section)
        if current == -1:
            result.error(f"Missing section: {section}")
        elif current <= position:
            result.error(f"Section out of order: {section}")
        position = max(position, current)

    if text.count("<details>") != 5 or text.count("</details>") != 5:
        result.error("Expected one static drawer and four evidence drawers.")
    if text.count("<summary><strong>Inspect ") != 4:
        result.error("Expected four evidence drawer summaries.")
    if '<table role="presentation">' in text or "```mermaid" in text:
        result.error("Legacy project-card table or profile Mermaid diagram detected.")
    if TOOL_ROW not in text:
        result.error("Approved nine-tool row is missing.")
    if text.count('href="#60-second-profile"') < 2:
        result.error("Motion and static hero assets must link to the 60-second profile.")

    for name in ("Yash Kanadhia", "Alexis Gorospe", "Sarmad Tariq"):
        if name not in text:
            result.error(f"PerFin attribution missing: {name}")
    if "This profile does not imply solo ownership." not in text:
        result.error("PerFin ownership guardrail is missing.")

    for boundary in (
        "does not connect to bank accounts or process payments",
        "does not claim an App Store release or a deployed production backend",
        "portfolio prototype, not a production OTT platform",
        "Checkout and rental completion are simulated",
    ):
        if boundary not in text:
            result.error(f"Required boundary missing: {boundary}")

    motion = validate_svg(MOTION, result)
    static = validate_svg(STATIC, result)
    if not DECISION.is_file() or DECISION.stat().st_size == 0:
        result.error(f"Missing required decision record: {DECISION.relative_to(ROOT)}")
    for asset in (*MEDIA, *PORTALS):
        validate_svg(asset, result)

    for item in (*LOCKED, *METRICS, *TOOLS):
        if item not in motion:
            result.error(f"Motion hero missing: {item}")
        if item not in static:
            result.error(f"Static hero missing: {item}")
    if "prefers-reduced-motion: reduce" not in motion:
        result.error("Reduced-motion handling is missing.")
    if "@keyframes" not in motion:
        result.error("Motion hero contains no animation.")
    if "@keyframes" in static:
        result.error("Static hero must not contain animation.")

    anchors = {slug(match.group(2)) for match in HEADING.finditer(text)}
    anchors.update(match.group(1).lower() for match in EXPLICIT_ID.finditer(text))
    for match in LINK.finditer(text):
        href = match.group("href")
        if href.startswith("#") and href[1:].lower() not in anchors:
            result.error(f"Broken internal anchor: {href}")

    for match in IMG.finditer(text):
        attrs = {a.group("name").lower(): a.group("value") for a in ATTR.finditer(match.group("attrs"))}
        if not attrs.get("src") or not attrs.get("alt", "").strip():
            result.error("README image is missing src or alt text.")

    self_path = Path(__file__).resolve()
    for path in ROOT.rglob("*"):
        if path.resolve() == self_path or not path.is_file():
            continue
        if any(part in {".git", ".venv", "node_modules", "__pycache__"} for part in path.parts):
            continue
        if path.suffix.lower() not in {".md", ".py", ".json", ".yml", ".yaml", ".svg", ".txt"}:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in SECRET:
            if pattern.search(content):
                result.error(f"Possible secret in {path.relative_to(ROOT)}")
        for pattern in PRIVATE:
            if pattern.search(content):
                result.error(f"Private path in {path.relative_to(ROOT)}")

    result.ok("Copy, structure, ownership, theme assets, links, and hygiene checked.")


def render(result: Result, as_json: bool) -> None:
    payload = {
        "release_ready": not result.errors,
        "errors": result.errors,
        "warnings": result.warnings,
        "checks": result.checks,
    }
    if as_json:
        print(json.dumps(payload, indent=2))
        return
    print("Profile dual-layer theme-system release validation")
    print(f"Result: {'PASS' if not result.errors else 'BLOCKED'}")
    for item in result.checks:
        print(f"  OK: {item}")
    for item in result.warnings:
        print(f"  WARNING: {item}")
    for item in result.errors:
        print(f"  ERROR: {item}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--online", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    result = Result()
    if not README.is_file():
        result.error("README.md is missing.")
    else:
        validate(README.read_text(encoding="utf-8"), result)
    if args.online:
        result.warn("Definitive online link checking is handled by validate_profile_links.py.")
    render(result, args.json)
    return 1 if result.errors else 0


if __name__ == "__main__":
    sys.exit(main())
