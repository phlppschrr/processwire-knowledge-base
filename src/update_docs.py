#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
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
        help="ProcessWire branch to fetch",
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
            str(docs_root / "core"),
            "--profile",
            "core",
        ]
    )

    run(
        build_docs
        + [
            "--out",
            str(docs_root / "full"),
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
            str(docs_root / "guides"),
        ]
        if args.fetch:
            guides_cmd.append("--fetch")
        run(guides_cmd)

    run(
        [
            sys.executable,
            str(ROOT_DIR / "src/build_tasks.py"),
            "--core",
            str(docs_root / "core"),
            "--full",
            str(docs_root / "full"),
            "--tasks",
            args.tasks,
            "--out",
            str(docs_root),
        ]
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
