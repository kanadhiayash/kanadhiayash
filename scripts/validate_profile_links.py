#!/usr/bin/env python3
"""Validate public README links without treating broken HEAD behavior as a 404."""

from __future__ import annotations

import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
USER_AGENT = "kanadhiayash-profile-link-validator/1.0"
TIMEOUT_SECONDS = 20

MD_LINK = re.compile(
    r"(?<!!)\[[^\]]+\]\((?P<href>[^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\)"
)
HTML_LINK = re.compile(r"<a\b[^>]*\bhref=[\"'](?P<href>[^\"']+)[\"']", re.I)


def external_links(text: str) -> list[str]:
    links = {match.group("href") for match in MD_LINK.finditer(text)}
    links.update(match.group("href") for match in HTML_LINK.finditer(text))
    return sorted(
        link
        for link in links
        if urllib.parse.urlparse(link).scheme == "https"
    )


def request_url(url: str, method: str) -> int:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
    }
    if method == "GET":
        headers["Range"] = "bytes=0-1023"
    request = urllib.request.Request(url, headers=headers, method=method)
    with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        if method == "GET":
            response.read(1024)
        return int(getattr(response, "status", 200))


def confirm_url(url: str) -> tuple[str, str]:
    """Return status category and detail: ok, warning, or error."""

    try:
        status = request_url(url, "HEAD")
        if status < 400:
            return "ok", f"HTTP {status}"
    except urllib.error.HTTPError as exc:
        head_detail = f"HEAD HTTP {exc.code}"
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        head_detail = f"HEAD inconclusive: {exc}"
    else:
        head_detail = f"HEAD HTTP {status}"

    try:
        status = request_url(url, "GET")
        if status < 400:
            return "ok", f"GET confirmed HTTP {status} after {head_detail}"
        return "warning", f"GET returned HTTP {status} after {head_detail}"
    except urllib.error.HTTPError as exc:
        if exc.code in {404, 410}:
            return "error", f"GET confirmed HTTP {exc.code} after {head_detail}"
        return "warning", f"GET could not be confirmed (HTTP {exc.code}) after {head_detail}"
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return "warning", f"GET inconclusive after {head_detail}: {exc}"


def main() -> int:
    if not README.is_file():
        print("ERROR: README.md is missing.")
        return 1

    urls = external_links(README.read_text(encoding="utf-8"))
    errors: list[str] = []
    warnings: list[str] = []

    print(f"Checking {len(urls)} external README links.")
    for url in urls:
        category, detail = confirm_url(url)
        if category == "ok":
            print(f"OK: {url} ({detail})")
        elif category == "warning":
            warnings.append(f"{url} ({detail})")
        else:
            errors.append(f"{url} ({detail})")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"Result: BLOCKED, {len(errors)} definitive broken link(s).")
        return 1

    print(f"Result: PASS, with {len(warnings)} inconclusive warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
