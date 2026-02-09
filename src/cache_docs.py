#!/usr/bin/env python3
"""Cache ProcessWire docs HTML locally for offline analysis."""
from __future__ import annotations

import argparse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


@dataclass
class CacheResult:
    url: str
    path: str
    status: str
    fetched_at: str
    status_code: int | None = None
    content_type: str | None = None
    bytes: int | None = None
    error: str | None = None


def load_urls(path: Path) -> list[str]:
    urls: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        urls.append(stripped)
    return urls


def url_to_relpath(url: str) -> str:
    parsed = urlparse(url)
    host = parsed.netloc or "processwire.com"
    path = parsed.path or "/"
    if path.endswith("/"):
        path = f"{path}index.html"
    elif not path.endswith(".html"):
        path = f"{path}/index.html"
    if parsed.query:
        safe_query = parsed.query.replace("/", "_").replace("&", "_").replace("=", "-")
        path = f"{path}__{safe_query}"
    return f"{host}{path}"


def fetch_url(url: str, out_path: Path, refresh: bool, timeout: float) -> CacheResult:
    fetched_at = datetime.now(timezone.utc).isoformat()
    if out_path.exists() and not refresh:
        size = out_path.stat().st_size
        return CacheResult(
            url=url,
            path=str(out_path),
            status="cached",
            fetched_at=fetched_at,
            bytes=size,
        )
    try:
        req = Request(
            url,
            headers={
                "User-Agent": "processwire-knowledge-base/0.1 (+https://processwire.com/)"
            },
        )
        with urlopen(req, timeout=timeout) as resp:
            body = resp.read()
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_bytes(body)
            return CacheResult(
                url=url,
                path=str(out_path),
                status="fetched",
                fetched_at=fetched_at,
                status_code=getattr(resp, "status", None),
                content_type=resp.headers.get("Content-Type"),
                bytes=len(body),
            )
    except HTTPError as exc:
        return CacheResult(
            url=url,
            path=str(out_path),
            status="error",
            fetched_at=fetched_at,
            status_code=exc.code,
            error=str(exc),
        )
    except URLError as exc:
        return CacheResult(
            url=url,
            path=str(out_path),
            status="error",
            fetched_at=fetched_at,
            error=str(exc),
        )


def write_index(results: Iterable[CacheResult], out_dir: Path) -> None:
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "items": [asdict(result) for result in results],
    }
    (out_dir / "_index.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def fetch_urls(
    url_path: Path,
    out_dir: Path,
    refresh: bool = False,
    sleep: float = 0.5,
    timeout: float = 30.0,
    workers: int = 1,
    reporter: Callable[[str], None] | None = None,
) -> tuple[list[CacheResult], dict]:
    if not url_path.exists():
        raise FileNotFoundError(f"URL list not found: {url_path}")

    urls = load_urls(url_path)
    if not urls:
        raise ValueError("No URLs to fetch.")

    results: list[CacheResult | None] = [None] * len(urls)
    fetched = cached = failed = 0

    def run_one(index: int, url: str) -> tuple[int, CacheResult, Path]:
        rel = url_to_relpath(url)
        out_path = out_dir / rel
        return index, fetch_url(url, out_path, refresh, timeout), out_path

    max_workers = max(1, int(workers))
    max_workers = min(max_workers, len(urls))

    if max_workers == 1:
        for idx, url in enumerate(urls, start=1):
            _, result, out_path = run_one(idx - 1, url)
            results[idx - 1] = result
            if result.status == "fetched":
                fetched += 1
            elif result.status == "cached":
                cached += 1
            else:
                failed += 1
            if reporter:
                reporter(
                    f"[{idx}/{len(urls)}] {result.status.upper()}: {url} -> {out_path}"
                )
            if idx < len(urls) and sleep:
                time.sleep(sleep)
    else:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for idx, url in enumerate(urls, start=1):
                futures.append(executor.submit(run_one, idx - 1, url))
                if idx < len(urls) and sleep:
                    time.sleep(sleep)
            for future in as_completed(futures):
                index, result, out_path = future.result()
                results[index] = result
                if result.status == "fetched":
                    fetched += 1
                elif result.status == "cached":
                    cached += 1
                else:
                    failed += 1
                if reporter:
                    reporter(
                        f"[{index + 1}/{len(urls)}] {result.status.upper()}: {result.url} -> {out_path}"
                    )

    out_dir.mkdir(parents=True, exist_ok=True)
    if any(result is None for result in results):
        raise RuntimeError("Fetch results incomplete.")
    write_index([result for result in results if result is not None], out_dir)

    stats = {
        "fetched": fetched,
        "cached": cached,
        "failed": failed,
        "index": str(out_dir / "_index.json"),
    }
    return results, stats


def main() -> int:
    parser = argparse.ArgumentParser(description="Cache ProcessWire docs HTML")
    parser.add_argument(
        "--urls",
        default="sources/urls.txt",
        help="Path to URL list (default: sources/urls.txt)",
    )
    parser.add_argument(
        "--out",
        default="sources/docs-html",
        help="Output directory (default: sources/docs-html)",
    )
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Re-download even if file exists",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=0.5,
        help="Sleep between requests in seconds (default: 0.5)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="Request timeout in seconds (default: 30)",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Number of parallel workers (default: 1)",
    )

    args = parser.parse_args()
    url_path = Path(args.urls)
    out_dir = Path(args.out)

    try:
        _, stats = fetch_urls(
            url_path,
            out_dir,
            refresh=args.refresh,
            sleep=args.sleep,
            timeout=args.timeout,
            workers=args.workers,
            reporter=lambda msg: print(msg, file=sys.stderr),
        )
    except (FileNotFoundError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    print(
        f"Done. fetched={stats['fetched']} cached={stats['cached']} failed={stats['failed']} index={stats['index']}",
        file=sys.stderr,
    )
    return 0 if stats["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
