#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path

DEFAULT_SOURCE = (
    Path(__file__).resolve().parents[1]
    / "sources/processwire/wire/core/ProcessWire.php"
)

VERSION_RE = {
    "major": re.compile(r"const\s+versionMajor\s*=\s*(\d+)", re.I),
    "minor": re.compile(r"const\s+versionMinor\s*=\s*(\d+)", re.I),
    "revision": re.compile(r"const\s+versionRevision\s*=\s*(\d+)", re.I),
    "suffix": re.compile(r"const\s+versionSuffix\s*=\s*'([^']*)'", re.I),
}


def _slug(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def parse_version(text: str) -> tuple[str, str | None]:
    major = VERSION_RE["major"].search(text)
    minor = VERSION_RE["minor"].search(text)
    revision = VERSION_RE["revision"].search(text)
    suffix_match = VERSION_RE["suffix"].search(text)

    if not (major and minor and revision):
        raise SystemExit("Could not find versionMajor/minor/revision in ProcessWire.php")

    version = f"{major.group(1)}.{minor.group(1)}.{revision.group(1)}"
    suffix = None
    if suffix_match:
        raw = suffix_match.group(1).strip()
        if raw:
            suffix = _slug(raw)
    return version, suffix


def build_tag(version: str, suffix: str | None, date_str: str) -> str:
    if suffix:
        return f"pw-{version}-{suffix}-{date_str}"
    return f"pw-{version}-{date_str}"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a ProcessWire-based release tag with date"
    )
    parser.add_argument(
        "--source",
        default=str(DEFAULT_SOURCE),
        help="Path to ProcessWire.php (default: sources/processwire/wire/core/ProcessWire.php)",
    )
    parser.add_argument(
        "--date",
        default=None,
        help="Override date (YYYY-MM-DD). Defaults to today in local time.",
    )
    args = parser.parse_args()

    source = Path(args.source)
    if not source.exists():
        raise SystemExit(f"Source file not found: {source}")

    if args.date:
        date_str = args.date
    else:
        date_str = dt.date.today().strftime("%Y-%m-%d")

    text = source.read_text(encoding="utf-8", errors="ignore")
    version, suffix = parse_version(text)
    tag = build_tag(version, suffix, date_str)
    print(tag)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
