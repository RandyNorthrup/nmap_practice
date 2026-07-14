#!/usr/bin/env python3
"""Repeat a validated profile and report XML changes between bounded runs.

Minimum interval is five seconds and maximum run count is 100. This prevents an
accidental infinite scanner. Scope/risk locks from selected profile still apply.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import time

from compare_results import compare, parse_report
from profile_runner import run_profile
from profiles import PROFILES


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", help="Profile name; use profile_catalog.py")
    parser.add_argument("target")
    parser.add_argument("--interval", type=float, default=60.0, help="Seconds (minimum 5)")
    parser.add_argument("--count", type=int, default=2, help="Runs (2-100)")
    parser.add_argument("--output-dir", default="results/watch")
    parser.add_argument("--allow-public", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    item = PROFILES.get(args.profile)
    if item is None:
        parser.error(f"Unknown profile: {args.profile}")
    if not 2 <= args.count <= 100:
        parser.error("--count must be between 2 and 100")
    if args.interval < 5 and not args.dry_run:
        parser.error("--interval must be at least 5 seconds")

    safe_target = re.sub(r"[^A-Za-z0-9._-]", "_", args.target)
    previous: Path | None = None
    for index in range(1, args.count + 1):
        prefix = Path(args.output_dir) / f"{safe_target}-{index:03d}"
        argv = [args.target, "--output", str(prefix)]
        if args.allow_public:
            argv.append("--allow-public")
        if args.dry_run:
            argv.append("--dry-run")
        code = run_profile(item, argv)
        if code:
            return code
        current = prefix.with_suffix(".xml")
        if not args.dry_run and previous is not None:
            changes = compare(parse_report(previous), parse_report(current))
            print(f"Run {index}: {len(changes)} change(s)")
            print(*changes, sep="\n")
        previous = current
        if index < args.count and not args.dry_run:
            time.sleep(args.interval)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
