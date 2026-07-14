#!/usr/bin/env python3
"""Repeat a validated profile at a safe interval to build comparison reports."""

from __future__ import annotations

import argparse
import time

from profile_runner import run_profile
from profiles import PROFILES


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", choices=sorted(PROFILES))
    parser.add_argument("target")
    parser.add_argument("--count", type=int, default=3, help="Runs, 1-100 (default: 3)")
    parser.add_argument("--interval", type=int, default=60, help="Seconds, 10-86400 (default: 60)")
    parser.add_argument("--allow-public", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if not 1 <= args.count <= 100:
        parser.error("--count must be between 1 and 100")
    if not 10 <= args.interval <= 86400:
        parser.error("--interval must be between 10 and 86400 seconds")

    failures = 0
    try:
        for run_number in range(1, args.count + 1):
            print(f"\nRun {run_number}/{args.count}")
            argv = [args.target]
            if args.allow_public:
                argv.append("--allow-public")
            if args.dry_run:
                argv.append("--dry-run")
            failures += run_profile(PROFILES[args.profile], argv) != 0
            if run_number < args.count and not args.dry_run:
                time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nStopped by user.")
        return 130
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
