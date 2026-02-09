#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import subprocess
from pathlib import Path

DEFAULT_REMOTE = "git@github.com:processwire/processwire.git"


def run_git(args: list[str], cwd: Path | None = None, capture: bool = False) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=str(cwd) if cwd else None,
        check=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=None,
        text=True,
    )
    return result.stdout.strip() if capture and result.stdout else ""


def is_git_repo(path: Path) -> bool:
    try:
        subprocess.run(
            ["git", "-C", str(path), "rev-parse", "--is-inside-work-tree"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            text=True,
        )
        return True
    except subprocess.CalledProcessError:
        return False


def next_backup_path(path: Path) -> Path:
    base = Path(f"{path}.backup")
    if not base.exists():
        return base
    idx = 1
    while True:
        candidate = Path(f"{base}.{idx}")
        if not candidate.exists():
            return candidate
        idx += 1


def sync_processwire(
    source_dir: Path,
    branch: str,
    remote_url: str,
    update: bool = True,
    lock_path: Path | None = None,
) -> str:
    if not source_dir.exists():
        source_dir.parent.mkdir(parents=True, exist_ok=True)
        run_git(["clone", "--branch", branch, remote_url, str(source_dir)])
    else:
        if not is_git_repo(source_dir):
            backup_dir = next_backup_path(source_dir)
            source_dir.rename(backup_dir)
            run_git(["clone", "--branch", branch, remote_url, str(source_dir)])
        elif update:
            run_git(["fetch", "origin"], cwd=source_dir)
            run_git(["checkout", branch], cwd=source_dir)
            run_git(["pull", "--ff-only", "origin", branch], cwd=source_dir)

    commit_sha = run_git(["rev-parse", "HEAD"], cwd=source_dir, capture=True)

    if lock_path:
        lock_path.parent.mkdir(parents=True, exist_ok=True)
        lock_path.write_text(
            f"branch={branch}\ncommit={commit_sha}\n",
            encoding="utf-8",
        )
    return commit_sha


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync ProcessWire source repository")
    parser.add_argument(
        "--source",
        default="sources/processwire",
        help="Path to ProcessWire source root (default: sources/processwire)",
    )
    parser.add_argument(
        "--branch",
        default=os.getenv("PW_SOURCE_BRANCH", "dev"),
        help="Branch to sync (default: PW_SOURCE_BRANCH or 'dev')",
    )
    parser.add_argument(
        "--remote",
        default=os.getenv("PW_SOURCE_REMOTE", DEFAULT_REMOTE),
        help=f"Git remote URL (default: {DEFAULT_REMOTE})",
    )
    parser.add_argument(
        "--lock",
        default=None,
        help="Write lock file (default: <source>/../processwire.lock)",
    )
    parser.add_argument(
        "--no-update",
        action="store_true",
        help="Do not fetch/pull when repo exists",
    )
    args = parser.parse_args()

    source_dir = Path(args.source)
    lock_path = Path(args.lock) if args.lock else source_dir.parent / "processwire.lock"

    commit = sync_processwire(
        source_dir=source_dir,
        branch=args.branch,
        remote_url=args.remote,
        update=not args.no_update,
        lock_path=lock_path,
    )

    print(f"ProcessWire source synced: {args.branch} @ {commit}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
