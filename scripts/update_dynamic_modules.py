#!/usr/bin/env python3
"""Update bounded dynamic sections in the GitHub profile README.

The script uses only Python's standard library. It updates content only between
explicit markers and preserves the last reviewed content when a remote source
cannot be fetched or parsed.
"""

from __future__ import annotations

import argparse
import email.utils
import html
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
CONFIG_PATH = ROOT / "data" / "profile_sources.json"

WRITING_START = "<!-- DYNAMIC:WRITING:START -->"
WRITING_END = "<!-- DYNAMIC:WRITING:END -->"
SIGNALS_START = "<!-- DYNAMIC:SIGNALS:START -->"
SIGNALS_END = "<!-- DYNAMIC:SIGNALS:END -->"

USER_AGENT = "kanadhiayash-profile-refresh/1.0"
TIMEOUT_SECONDS = 20


@dataclass(frozen=True)
class Item:
    title: str
    url: str
    date: datetime | None = None
    label: str | None = None


def load_config() -> dict[str, Any]:
    with CONFIG_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require_https(url: str, allowed_hosts: Iterable[str]) -> str:
    parsed = urllib.parse.urlparse(url)
    host = (parsed.hostname or "").lower()
    if parsed.scheme != "https":
        raise ValueError(f"Only HTTPS sources are allowed: {url}")
    allowed = any(host == entry or host.endswith(f".{entry}") for entry in allowed_hosts)
    if not allowed:
        raise ValueError(f"Source host is not allowlisted: {host}")
    return url


def fetch_bytes(url: str, *, github_token: str | None = None) -> bytes:
    headers = {
        "Accept": "application/json, application/atom+xml, application/rss+xml, application/xml, text/xml",
        "User-Agent": USER_AGENT,
    }
    if github_token and urllib.parse.urlparse(url).hostname == "api.github.com":
        headers["Authorization"] = f"Bearer {github_token}"
        headers["X-GitHub-Api-Version"] = "2022-11-28"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        return response.read()


def clean_text(value: str) -> str:
    value = html.unescape(value or "")
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def markdown_text(value: str) -> str:
    value = clean_text(value)
    return value.replace("[", "\\[").replace("]", "\\]").replace("|", "\\|")


def parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    value = value.strip()
    try:
        parsed = email.utils.parsedate_to_datetime(value)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except (TypeError, ValueError):
        pass
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except ValueError:
        return None


def child_text(element: ET.Element, names: set[str]) -> str | None:
    for child in element:
        local_name = child.tag.rsplit("}", 1)[-1]
        if local_name in names and child.text:
            return child.text.strip()
    return None


def parse_feed(payload: bytes) -> list[Item]:
    root = ET.fromstring(payload)
    items: list[Item] = []
    candidates = [
        element
        for element in root.iter()
        if element.tag.rsplit("}", 1)[-1] in {"item", "entry"}
    ]
    for entry in candidates:
        title = child_text(entry, {"title"})
        date_value = child_text(entry, {"pubDate", "published", "updated"})
        link: str | None = None
        for child in entry:
            if child.tag.rsplit("}", 1)[-1] != "link":
                continue
            href = child.attrib.get("href")
            rel = child.attrib.get("rel", "alternate")
            if href and rel in {"alternate", ""}:
                link = href
                break
            if child.text and not link:
                link = child.text.strip()
        if not title or not link:
            continue
        try:
            safe_link = require_https(link, {"substack.com"})
        except ValueError:
            continue
        items.append(Item(title=clean_text(title), url=safe_link, date=parse_date(date_value)))
    items.sort(
        key=lambda item: item.date or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )
    return items


def fetch_writing(config: dict[str, Any]) -> list[Item]:
    errors: list[str] = []
    for candidate in config["feed_candidates"]:
        try:
            url = require_https(candidate, {"substack.com"})
            items = parse_feed(fetch_bytes(url))
            if items:
                return items[: int(config["max_items"])]
            errors.append(f"no items from {url}")
        except (ET.ParseError, OSError, ValueError, urllib.error.URLError) as exc:
            errors.append(f"{candidate}: {exc}")
    print("warning: writing feed unavailable; preserving reviewed README content", file=sys.stderr)
    for error in errors:
        print(f"warning: {error}", file=sys.stderr)
    return []


def github_api(path: str) -> str:
    return require_https(f"https://api.github.com/{path.lstrip('/')}", {"api.github.com"})


def fetch_json(url: str, token: str | None) -> Any:
    return json.loads(fetch_bytes(url, github_token=token).decode("utf-8"))


def fetch_release(source: dict[str, Any], token: str | None) -> Item | None:
    payload = fetch_json(github_api(f"repos/{source['repository']}/releases/latest"), token)
    title = clean_text(payload.get("name") or payload.get("tag_name") or "Release")
    return Item(
        title=title,
        url=require_https(payload["html_url"], {"github.com"}),
        date=parse_date(payload.get("published_at")),
        label=source["label"],
    )


def fetch_merged_pr(source: dict[str, Any], token: str | None) -> Item | None:
    query = urllib.parse.urlencode(
        {
            "state": "closed",
            "base": source.get("base", "main"),
            "sort": "updated",
            "direction": "desc",
            "per_page": 50,
        }
    )
    payload = fetch_json(
        github_api(f"repos/{source['repository']}/pulls?{query}"),
        token,
    )
    author = source.get("author")
    candidates = [
        pr
        for pr in payload
        if pr.get("merged_at")
        and (not author or pr.get("user", {}).get("login") == author)
    ]
    if not candidates:
        return None
    candidates.sort(key=lambda pr: pr["merged_at"], reverse=True)
    pr = candidates[0]
    return Item(
        title=f"PR #{pr['number']}: {clean_text(pr['title'])}",
        url=require_https(pr["html_url"], {"github.com"}),
        date=parse_date(pr.get("merged_at")),
        label=source["label"],
    )


def fetch_signals(config: dict[str, Any]) -> list[Item]:
    token = os.getenv("GITHUB_TOKEN")
    items: list[Item] = []
    for source in config["sources"]:
        try:
            if source["kind"] == "release":
                item = fetch_release(source, token)
            elif source["kind"] == "merged_pr":
                item = fetch_merged_pr(source, token)
            else:
                raise ValueError(f"Unsupported signal kind: {source['kind']}")
            if item:
                items.append(item)
        except (KeyError, OSError, ValueError, urllib.error.URLError, json.JSONDecodeError) as exc:
            print(
                f"warning: signal source failed for {source.get('repository')}: {exc}",
                file=sys.stderr,
            )
    items.sort(
        key=lambda item: item.date or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )
    return items[: int(config["max_items"])]


def format_date(value: datetime | None) -> str:
    if not value:
        return ""
    day = str(value.day)
    return f"{value.strftime('%B')} {day}, {value.year}"


def render_writing(items: list[Item], profile_url: str) -> str:
    lines = []
    for item in items:
        suffix = f" · {format_date(item.date)}" if item.date else ""
        lines.append(f"- [{markdown_text(item.title)}]({item.url}){suffix}")
    lines.append(f"- [View all writing on Substack]({profile_url})")
    return "\n".join(lines)


def render_signals(items: list[Item]) -> str:
    lines = []
    for item in items:
        suffix = f" · {format_date(item.date)}" if item.date else ""
        label = markdown_text(item.label or "Build signal")
        lines.append(f"- **{label}:** [{markdown_text(item.title)}]({item.url}){suffix}")
    return "\n".join(lines)


def validate_markers(readme: str) -> None:
    for start, end in ((WRITING_START, WRITING_END), (SIGNALS_START, SIGNALS_END)):
        if readme.count(start) != 1 or readme.count(end) != 1:
            raise ValueError(f"README must contain exactly one {start} and one {end}")
        if readme.index(start) >= readme.index(end):
            raise ValueError(f"README marker order is invalid for {start}")


def replace_region(readme: str, start: str, end: str, body: str) -> str:
    pattern = re.compile(rf"{re.escape(start)}.*?{re.escape(end)}", re.DOTALL)
    replacement = f"{start}\n{body.rstrip()}\n{end}"
    updated, count = pattern.subn(replacement, readme, count=1)
    if count != 1:
        raise ValueError(f"Unable to update README region: {start}")
    return updated


def validate_config(config: dict[str, Any]) -> None:
    writing = config["writing"]
    signals = config["signals"]
    require_https(writing["profile_url"], {"substack.com"})
    for feed in writing["feed_candidates"]:
        require_https(feed, {"substack.com"})
    if not 1 <= int(writing["max_items"]) <= 5:
        raise ValueError("writing.max_items must be between 1 and 5")
    if not 1 <= int(signals["max_items"]) <= 5:
        raise ValueError("signals.max_items must be between 1 and 5")
    for source in signals["sources"]:
        if source["kind"] not in {"release", "merged_pr"}:
            raise ValueError(f"Unsupported source kind: {source['kind']}")
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", source["repository"]):
            raise ValueError(f"Invalid repository name: {source['repository']}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate config and README markers without network access",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Fetch sources and update README regions",
    )
    args = parser.parse_args()
    if args.check == args.write:
        parser.error("choose exactly one of --check or --write")

    config = load_config()
    validate_config(config)
    readme = README_PATH.read_text(encoding="utf-8")
    validate_markers(readme)

    if args.check:
        print("profile dynamic module structure is valid")
        return 0

    writing_items = fetch_writing(config["writing"])
    signal_items = fetch_signals(config["signals"])
    updated = readme
    if writing_items:
        updated = replace_region(
            updated,
            WRITING_START,
            WRITING_END,
            render_writing(writing_items, config["writing"]["profile_url"]),
        )
    if signal_items:
        updated = replace_region(
            updated,
            SIGNALS_START,
            SIGNALS_END,
            render_signals(signal_items),
        )
    if updated != readme:
        README_PATH.write_text(updated, encoding="utf-8")
        print("README dynamic modules updated")
    else:
        print("no dynamic module changes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
