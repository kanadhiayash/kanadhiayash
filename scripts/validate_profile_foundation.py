#!/usr/bin/env python3
"""Run the profile validator while treating hero placement as a known warning.

This proves that all non-hero release checks pass while the strict release job
continues to block publication until the approved hero bundle is committed.
"""

from __future__ import annotations

import sys

import validate_profile_release as gate

HERO_BLOCKER_TOKENS = (
    "assets/hero/yash-kanadhia-living-product-console-dark",
    "approved hero PNG",
    "Hero alt text",
    "Hero PNG",
    "Hero JPG",
    "Hero SVG",
)

_original_error = gate.Result.error


def foundation_error(self: gate.Result, message: str) -> None:
    if any(token in message for token in HERO_BLOCKER_TOKENS):
        self.warn(f"Known hero-placement blocker: {message}")
        return
    _original_error(self, message)


gate.Result.error = foundation_error

if __name__ == "__main__":
    sys.exit(gate.main())
