#!/usr/bin/env python3
"""Validate the Living Product Console motion system using only the standard library."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

PAIRS = (
    (
        ROOT / "assets/hero/yash-kanadhia-living-product-console-dark-motion.svg",
        ROOT / "assets/hero/yash-kanadhia-living-product-console-dark.png",
        "./assets/hero/yash-kanadhia-living-product-console-dark-motion.svg",
        "./assets/hero/yash-kanadhia-living-product-console-dark.png",
    ),
    (
        ROOT / "assets/projects/flagship-systems-motion.svg",
        ROOT / "assets/projects/flagship-systems.svg",
        "./assets/projects/flagship-systems-motion.svg",
        "./assets/projects/flagship-systems.svg",
    ),
    (
        ROOT / "assets/projects/built-product-proof-motion.svg",
        ROOT / "assets/projects/built-product-proof.svg",
        "./assets/projects/built-product-proof-motion.svg",
        "./assets/projects/built-product-proof.svg",
    ),
    (
        ROOT / "assets/projects/product-design-studies-motion.svg",
        ROOT / "assets/projects/product-design-studies.svg",
        "./assets/projects/product-design-studies-motion.svg",
        "./assets/projects/product-design-studies.svg",
    ),
)

DURATION = re.compile(r'\bdur=["\'](?P<value>\d+(?:\.\d+)?)s["\']')
FORBIDDEN = ("<script", "javascript:", "onload=", "onclick=", "<foreignObject")


def error(message: str, errors: list[str]) -> None:
    errors.append(message)


def validate_svg(path: Path, errors: list[str]) -> None:
    if not path.is_file() or path.stat().st_size == 0:
        error(f"Motion asset missing or empty: {path.relative_to(ROOT)}", errors)
        return

    text = path.read_text(encoding="utf-8")
    lowered = text.lower()

    if "<svg" not in text or 'role="img"' not in text:
        error(f"Motion SVG must contain an SVG root and role=img: {path.relative_to(ROOT)}", errors)
    if "<title" not in text or "<desc" not in text:
        error(f"Motion SVG must contain title and description elements: {path.relative_to(ROOT)}", errors)
    if not any(token in text for token in ("<animate", "<animateMotion", "@keyframes")):
        error(f"Motion SVG contains no detectable animation: {path.relative_to(ROOT)}", errors)

    for token in FORBIDDEN:
        if token.lower() in lowered:
            error(f"Unsafe or unsupported SVG token {token}: {path.relative_to(ROOT)}", errors)

    for match in DURATION.finditer(text):
        duration = float(match.group("value"))
        if duration < 4.0:
            error(
                f"Animation duration below four seconds in {path.relative_to(ROOT)}: {duration}s",
                errors,
            )


def validate_readme(text: str, errors: list[str]) -> None:
    last_position = -1
    for motion, static, motion_ref, static_ref in PAIRS:
        validate_svg(motion, errors)
        if not static.is_file() or static.stat().st_size == 0:
            error(f"Static alternative missing or empty: {static.relative_to(ROOT)}", errors)

        if text.count(motion_ref) != 1:
            error(f"README must reference motion asset exactly once: {motion_ref}", errors)
        if text.count(static_ref) != 1:
            error(f"README must reference static alternative exactly once: {static_ref}", errors)

        motion_position = text.find(motion_ref)
        static_position = text.find(static_ref)
        if motion_position == -1 or static_position == -1:
            continue
        if motion_position <= last_position:
            error(f"Motion asset is out of expected page order: {motion_ref}", errors)
        if static_position < motion_position:
            error(f"Static alternative must follow its motion asset: {static_ref}", errors)
        last_position = motion_position

    if text.count("<details>") < 4:
        error("README must provide expandable static alternatives for all four motion surfaces.", errors)
    if "Slow ambient motion only" not in text:
        error("README motion disclosure is missing.", errors)


def main() -> int:
    errors: list[str] = []
    if not README.is_file():
        error("README.md is missing.", errors)
    else:
        validate_readme(README.read_text(encoding="utf-8"), errors)

    print("Profile motion validation")
    if errors:
        print("Result: BLOCKED")
        for item in errors:
            print(f"  ERROR: {item}")
        return 1

    print("Result: PASS")
    print("  OK: Four motion surfaces are present and ordered.")
    print("  OK: Four static alternatives are present and ordered.")
    print("  OK: Motion assets contain accessible metadata and slow animation timings.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
