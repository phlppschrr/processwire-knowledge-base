#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import datetime as dt
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def add_opt(cmd: list[str], flag: str, value: str | None) -> None:
    if value is not None:
        cmd.extend([flag, value])


def main() -> int:
    parser = argparse.ArgumentParser(description="Build ProcessWire docs outputs")
    parser.add_argument(
        "--source",
        default="sources/processwire",
        help="Path to ProcessWire source root (default: sources/processwire)",
    )
    parser.add_argument(
        "--cache",
        default="sources/docs-html",
        help="HTML cache root (default: sources/docs-html)",
    )
    parser.add_argument(
        "--urls",
        default="sources/urls.txt",
        help="URL list (default: sources/urls.txt)",
    )
    parser.add_argument(
        "--docs",
        default="docs",
        help="Docs output root (default: docs)",
    )
    parser.add_argument(
        "--tasks",
        default="tasks.json",
        help="Tasks JSON (default: tasks.json)",
    )
    parser.add_argument(
        "--fetch",
        action="store_true",
        help="Fetch sources if missing or refresh existing",
    )
    parser.add_argument(
        "--guides",
        action="store_true",
        help="Build guide docs output (default: off)",
    )
    parser.add_argument(
        "--branch",
        default=None,
        choices=["dev", "master"],
        help="ProcessWire branch to fetch (dev or master)",
    )
    parser.add_argument(
        "--remote",
        default=None,
        help="ProcessWire git remote URL",
    )
    parser.add_argument(
        "--lock",
        default=None,
        help="ProcessWire lock file path",
    )
    args = parser.parse_args()

    docs_root = Path(args.docs)
    source_root = Path(args.source)

    build_docs = [
        sys.executable,
        str(ROOT_DIR / "src/build_docs.py"),
        "--source",
        args.source,
    ]
    if args.fetch:
        build_docs.append("--fetch")
    add_opt(build_docs, "--branch", args.branch)
    add_opt(build_docs, "--remote", args.remote)
    add_opt(build_docs, "--lock", args.lock)

    run(
        build_docs
        + [
            "--out",
            str(docs_root / "api-core"),
            "--profile",
            "core",
        ]
    )

    run(
        build_docs
        + [
            "--out",
            str(docs_root / "api-full"),
            "--profile",
            "full",
        ]
    )

    if args.guides:
        guides_cmd = [
            sys.executable,
            str(ROOT_DIR / "src/build_guides.py"),
            "--cache",
            args.cache,
            "--urls",
            args.urls,
            "--out",
            str(docs_root),
        ]
        if args.fetch:
            guides_cmd.append("--fetch")
        run(guides_cmd)

    run(
        [
            sys.executable,
            str(ROOT_DIR / "src/build_tasks.py"),
            "--core",
            str(docs_root / "api-core"),
            "--full",
            str(docs_root / "api-full"),
            "--tasks",
            args.tasks,
            "--out",
            str(docs_root),
        ]
    )

    write_version_meta(source_root, docs_root)

    return 0


def write_version_meta(source_root: Path, docs_root: Path) -> None:
    processwire_file = source_root / "wire/core/ProcessWire.php"
    if not processwire_file.exists():
        return
    text = processwire_file.read_text(encoding="utf-8", errors="ignore")
    version = extract_version(text)
    suffix = extract_suffix(text)
    if not version:
        return

    lock_path = source_root.parent / "processwire.lock"
    branch = None
    commit = None
    if lock_path.exists():
        for line in lock_path.read_text(encoding="utf-8").splitlines():
            if line.startswith("branch="):
                branch = line.split("=", 1)[1].strip() or None
            elif line.startswith("commit="):
                commit = line.split("=", 1)[1].strip() or None

    meta = {
        "version": version,
        "suffix": suffix,
        "branch": branch,
        "commit": commit,
        "generated": dt.date.today().strftime("%Y-%m-%d"),
    }
    out_path = docs_root / "_processwire_version.json"
    out_path.write_text(
        json.dumps(meta, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def extract_version(text: str) -> str | None:
    def find_const(name: str) -> str | None:
        match = re.search(rf"const\s+{name}\s*=\s*(\d+)", text, re.I)
        return match.group(1) if match else None

    major = find_const("versionMajor")
    minor = find_const("versionMinor")
    revision = find_const("versionRevision")
    if not (major and minor and revision):
        return None
    return f"{major}.{minor}.{revision}"


def extract_suffix(text: str) -> str | None:
    match = re.search(r"const\s+versionSuffix\s*=\s*'([^']*)'", text, re.I)
    if not match:
        return None
    raw = match.group(1).strip()
    return raw or None


if __name__ == "__main__":
    raise SystemExit(main())
