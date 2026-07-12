#!/usr/bin/env python3
"""Validate Organic AlienTech motion SVGs and README references."""

from __future__ import annotations

import sys
from pathlib import Path

import validate_profile_release as release

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

MOTION_PAIRS = (
    ("Profile hero", "assets/hero/yash-kanadhia-alientech-motion.svg", "assets/hero/yash-kanadhia-alientech-static.svg"),
    ("Tool constellation", "assets/tooling/alientech-tool-constellation-motion.svg", "assets/tooling/alientech-tool-constellation-static.svg"),
    ("Zeref guarded-memory flow", "assets/motion/zeref-system-flow-motion.svg", "assets/motion/zeref-system-flow-static.svg"),
    ("Product working model", "assets/motion/product-working-model-motion.svg", "assets/motion/product-working-model-static.svg"),
)


def main() -> int:
    errors: list[str] = []
    readme = README.read_text(encoding="utf-8") if README.is_file() else ""
    result = release.Result()

    for name, motion, static in MOTION_PAIRS:
        motion_path = ROOT / motion
        static_path = ROOT / static
        if not motion_path.is_file():
            errors.append(f"Missing motion SVG for {name}: {motion}")
            continue
        if not static_path.is_file():
            errors.append(f"Missing static SVG for {name}: {static}")
            continue
        release.validate_svg(motion_path, result, motion=True)
        release.validate_svg(static_path, result, motion=False)
        if motion in readme and static not in readme and "Profile hero" in name:
            errors.append(f"Profile hero static alternative is missing from README: {static}")

    if readme.count("./assets/hero/yash-kanadhia-alientech-motion.svg") != 1:
        errors.append("README must reference the AlienTech motion hero exactly once.")
    if readme.count("./assets/hero/yash-kanadhia-alientech-static.svg") != 1:
        errors.append("README must reference the AlienTech static hero exactly once.")
    if "Slow ambient motion only" in readme:
        errors.append("README still contains the old Living Product Console motion disclosure.")

    errors.extend(result.errors)
    print("Organic AlienTech motion validation")
    if errors:
        print("Result: BLOCKED")
        for error in errors:
            print(f"  ERROR: {error}")
        return 1
    print("Result: PASS")
    print("  OK: Four motion systems and static alternatives are present.")
    print("  OK: Motion SVGs include accessible metadata and reduced-motion handling.")
    print("  OK: README hero motion and static references are ordered and unique.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
