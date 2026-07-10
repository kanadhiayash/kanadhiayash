#!/usr/bin/env python3
"""Validate the staged interactive profile media contract using the standard library."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

HERO_MOTION = ROOT / "assets/hero/yash-kanadhia-living-product-console-dark-motion.svg"
HERO_STATIC = ROOT / "assets/hero/yash-kanadhia-living-product-console-dark.png"
HERO_MOTION_REF = "./assets/hero/yash-kanadhia-living-product-console-dark-motion.svg"
HERO_STATIC_REF = "./assets/hero/yash-kanadhia-living-product-console-dark.png"

PROJECTS = (
    (
        "PerFin OS",
        ROOT / "assets/projects/perfin-os/cover.svg",
        ROOT / "assets/projects/perfin-os/media-pending.svg",
        "./assets/projects/perfin-os/cover.svg",
        "./assets/projects/perfin-os/media-pending.svg",
    ),
    (
        "For Rent",
        ROOT / "assets/projects/for-rent/cover.svg",
        ROOT / "assets/projects/for-rent/media-pending.svg",
        "./assets/projects/for-rent/cover.svg",
        "./assets/projects/for-rent/media-pending.svg",
    ),
    (
        "StreamNexus",
        ROOT / "assets/projects/streamnexus/cover.svg",
        ROOT / "assets/projects/streamnexus/media-pending.svg",
        "./assets/projects/streamnexus/cover.svg",
        "./assets/projects/streamnexus/media-pending.svg",
    ),
)

DURATION = re.compile(r'\bdur=["\'](?P<value>\d+(?:\.\d+)?)s["\']')
FORBIDDEN = ("<script", "javascript:", "onload=", "onclick=", "<foreignobject")


def add_error(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_svg(path: Path, errors: list[str], *, motion: bool) -> None:
    if not path.is_file() or path.stat().st_size == 0:
        add_error(errors, f"SVG asset missing or empty: {path.relative_to(ROOT)}")
        return

    text = path.read_text(encoding="utf-8")
    lowered = text.lower()

    if "<svg" not in lowered or 'role="img"' not in lowered:
        add_error(errors, f"SVG must contain an SVG root and role=img: {path.relative_to(ROOT)}")
    if "<title" not in lowered or "<desc" not in lowered:
        add_error(errors, f"SVG must contain title and description elements: {path.relative_to(ROOT)}")

    for token in FORBIDDEN:
        if token in lowered:
            add_error(errors, f"Unsafe or unsupported SVG token {token}: {path.relative_to(ROOT)}")

    if not motion:
        return

    if not any(token in text for token in ("<animate", "<animateMotion", "@keyframes")):
        add_error(errors, f"Motion SVG contains no detectable animation: {path.relative_to(ROOT)}")

    for match in DURATION.finditer(text):
        duration = float(match.group("value"))
        if duration < 4.0:
            add_error(
                errors,
                f"Animation duration below four seconds in {path.relative_to(ROOT)}: {duration}s",
            )


def validate_readme(text: str, errors: list[str]) -> None:
    validate_svg(HERO_MOTION, errors, motion=True)
    if not HERO_STATIC.is_file() or HERO_STATIC.stat().st_size == 0:
        add_error(errors, f"Static hero missing or empty: {HERO_STATIC.relative_to(ROOT)}")

    if text.count(HERO_MOTION_REF) != 1:
        add_error(errors, "README must reference the motion hero exactly once.")
    if text.count(HERO_STATIC_REF) != 1:
        add_error(errors, "README must reference the static hero exactly once.")
    if text.find(HERO_STATIC_REF) < text.find(HERO_MOTION_REF):
        add_error(errors, "The static hero alternative must follow the motion hero.")

    last_cover_position = -1
    for name, cover, pending, cover_ref, pending_ref in PROJECTS:
        validate_svg(cover, errors, motion=False)
        validate_svg(pending, errors, motion=False)

        if text.count(cover_ref) != 1:
            add_error(errors, f"README must reference the {name} cover exactly once.")
        if text.count(pending_ref) != 1:
            add_error(errors, f"README must reference the {name} media state exactly once.")

        cover_position = text.find(cover_ref)
        pending_position = text.find(pending_ref)
        if cover_position <= last_cover_position:
            add_error(errors, f"Project cover is out of active order: {name}")
        if pending_position < cover_position:
            add_error(errors, f"Media state must follow the visible project cover: {name}")
        last_cover_position = cover_position

    if text.count("<details>") != 4:
        add_error(errors, "README must contain one static-hero drawer and three project case-file drawers.")
    if "Slow ambient motion only" not in text:
        add_error(errors, "README motion disclosure is missing.")
    if text.count("Verified walkthrough capture pending") != 0:
        add_error(
            errors,
            "Capture-state wording must remain inside accessible SVG metadata rather than duplicated as README image text.",
        )


def main() -> int:
    errors: list[str] = []
    if not README.is_file():
        add_error(errors, "README.md is missing.")
    else:
        validate_readme(README.read_text(encoding="utf-8"), errors)

    print("Profile staged-media validation")
    if errors:
        print("Result: BLOCKED")
        for item in errors:
            print(f"  ERROR: {item}")
        return 1

    print("Result: PASS")
    print("  OK: Motion hero and static alternative are present and ordered.")
    print("  OK: Three active project covers are present and ordered.")
    print("  OK: Three accessible media-capture states follow their covers.")
    print("  OK: README provides one identity drawer and three case-file drawers.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
