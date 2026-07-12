#!/usr/bin/env python3
"""Validate non-online GitHub profile release foundations."""

from __future__ import annotations

import sys

import validate_profile_release as release


if __name__ == "__main__":
    sys.exit(release.main())
