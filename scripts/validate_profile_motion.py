#!/usr/bin/env python3
"""Validate the dual-layer profile media and interaction contract."""

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

MEDIA_SLOTS = (
    ("Zeref Memory Engine", ROOT / "assets/profile-media/zeref-media-slot.svg", "./assets/profile-media/zeref-media-slot.svg"),
    ("PerFin OS", ROOT / "assets/profile-media/perfin-os-media-slot.svg", "./assets/profile-media/perfin-os-media-slot.svg"),
    ("For Rent", ROOT / "assets/profile-media/for-rent-media-slot.svg", "./assets/profile-media/for-rent-media-slot.svg"),
    ("StreamNexus", ROOT / "assets/profile-media/streamnexus-media-slot.svg", "./assets/profile-media/streamnexus-media-slot.svg"),
)

DURATION = re.compile(r'\bdur=["\'](?P<value>\d+(?:\.\d+)?)s["\']')
FORBIDDEN_SVG = ("<script", "javascript:", "onload=", "onclick=", "<foreignobject")
LEGACY_README_REFERENCES = (
    "./assets/projects/perfin-os/cover.svg",
    "./assets/projects/perfin-os/media-pending.svg",
    "./assets/projects/for-rent/cover.svg",
    "./assets/projects/for-rent/media-pending.svg",
    "./assets/projects/streamnexus/cover.svg",
    "./assets/projects/streamnexus/media-pending.svg",
)


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
    for token in FORBIDDEN_SVG:
        if token in lowered:
            add_error(errors, f"Unsafe or unsupported SVG token {token}: {path.relative_to(ROOT)}")

    if motion:
        if not any(token in text for token in ("<animate", "<animateMotion", "@keyframes")):
            add_error(errors, f"Motion SVG contains no detectable animation: {path.relative_to(ROOT)}")
        for match in DURATION.finditer(text):
            duration = float(match.group("value"))
            if duration < 4.0:
                add_error(errors, f"Animation duration below four seconds in {path.relative_to(ROOT)}: {duration}s")


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

    scan = text.find("## 60-second profile")
    evidence = text.find("## Deep evidence")
    if scan == -1 or evidence == -1 or scan >= evidence:
        add_error(errors, "The visible 60-second profile must precede Deep evidence.")

    for legacy in LEGACY_README_REFERENCES:
        if legacy in text:
            add_error(errors, f"Legacy thumbnail or media-state reference must not appear in README: {legacy}")

    last_position = evidence
    for name, path, reference in MEDIA_SLOTS:
        validate_svg(path, errors, motion=False)
        if text.count(reference) != 1:
            add_error(errors, f"README must reference the {name} media slot exactly once.")
            continue
        current = text.find(reference)
        if current <= last_position:
            add_error(errors, f"Media slot is missing or out of deep-evidence order: {name}")
        last_position = current

    if text.count("<details>") != 5 or text.count("</details>") != 5:
        add_error(errors, "README must contain one static-hero drawer and four evidence drawers.")
    if text.count("<summary><strong>Inspect ") != 4:
        add_error(errors, "README must provide exactly four evidence-drawer summaries.")
    if "Slow ambient motion only" not in text:
        add_error(errors, "README motion disclosure is missing.")
    if '<table role="presentation">' in text:
        add_error(errors, "README must not restore the compact project-card presentation table.")
    if "```mermaid" in text:
        add_error(errors, "README must keep architecture diagrams in project repositories, not the profile surface.")


def main() -> int:
    errors: list[str] = []
    if not README.is_file():
        add_error(errors, "README.md is missing.")
    else:
        validate_readme(README.read_text(encoding="utf-8"), errors)

    print("Profile dual-layer media validation")
    if errors:
        print("Result: BLOCKED")
        for item in errors:
            print(f"  ERROR: {item}")
        return 1

    print("Result: PASS")
    print("  OK: Motion hero and static alternative are present and ordered.")
    print("  OK: The visible 60-second profile precedes the deep-evidence layer.")
    print("  OK: Four accessible media slots are reserved inside evidence drawers.")
    print("  OK: Legacy thumbnail cards, duplicate covers, and profile Mermaid diagrams are absent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
