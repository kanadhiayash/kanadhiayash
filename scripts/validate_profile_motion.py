#!/usr/bin/env python3
"""Validate the approved adaptive samurai profile hero."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
MOTION = ROOT / "assets/hero/yash-kanadhia-living-product-console-dark-motion.svg"
STATIC = ROOT / "assets/hero/yash-kanadhia-living-product-console-dark.svg"
MOTION_REF = "./assets/hero/yash-kanadhia-living-product-console-dark-motion.svg"
STATIC_REF = "./assets/hero/yash-kanadhia-living-product-console-dark.svg"

LOCKED_FACTS = (
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

FORBIDDEN = ("<script", "javascript:", "onload=", "onclick=", "<foreignobject")
DURATION = re.compile(r"\b(?:animation-duration:|dur=[\"'])(\d+(?:\.\d+)?)s")


def validate_svg(path: Path, *, motion: bool, errors: list[str]) -> None:
    if not path.is_file() or path.stat().st_size == 0:
        errors.append(f"Missing or empty hero asset: {path.relative_to(ROOT)}")
        return

    text = path.read_text(encoding="utf-8")
    lower = text.lower()

    for token in ("<svg", 'role="img"', "<title", "<desc"):
        if token not in lower:
            errors.append(f"Missing SVG accessibility contract {token}: {path.relative_to(ROOT)}")

    for token in FORBIDDEN:
        if token in lower:
            errors.append(f"Unsafe SVG token {token}: {path.relative_to(ROOT)}")

    for value in (*LOCKED_FACTS, *METRICS, *TOOLS):
        if value not in text:
            errors.append(f"Hero asset missing approved content: {value}")

    if motion:
        if 'prefers-color-scheme: light' not in text:
            errors.append("Motion hero must include an adaptive light-mode palette.")
        if "@keyframes" not in text:
            errors.append("Motion hero contains no detectable animation.")
        if "prefers-reduced-motion: reduce" not in text:
            errors.append("Motion hero must include a reduced-motion rule.")
        for match in DURATION.finditer(text):
            if float(match.group(1)) < 4:
                errors.append(f"Hero animation duration below four seconds: {match.group(1)}s")
    elif "@keyframes" in text:
        errors.append("Static hero must not contain keyframe animation.")


def main() -> int:
    errors: list[str] = []

    if not README.is_file():
        errors.append("README.md is missing.")
    else:
        readme = README.read_text(encoding="utf-8")
        if readme.count(MOTION_REF) != 1:
            errors.append("README must reference the adaptive motion hero exactly once.")
        if readme.count(STATIC_REF) != 1:
            errors.append("README must reference the static hero exactly once.")
        if readme.find(STATIC_REF) < readme.find(MOTION_REF):
            errors.append("Static hero must follow the motion hero.")
        if readme.count('href="#60-second-profile"') < 2:
            errors.append("Motion and static hero assets must link to the 60-second profile.")
        expected_tools = "Figma · Linear · Notion · React · SwiftUI · Firebase · Claude · Codex · GitHub"
        if expected_tools not in readme:
            errors.append("README tool rail text does not match the approved nine-tool order.")

    validate_svg(MOTION, motion=True, errors=errors)
    validate_svg(STATIC, motion=False, errors=errors)

    print("Adaptive samurai hero validation")
    if errors:
        print("Result: BLOCKED")
        for error in errors:
            print(f"  ERROR: {error}")
        return 1

    print("Result: PASS")
    print("  OK: Locked Yash facts are preserved.")
    print("  OK: Approved metrics and nine-tool rail are present.")
    print("  OK: Light, dark, motion, reduced-motion, and static contracts are present.")
    print("  OK: Hero routes to the 60-second profile.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
