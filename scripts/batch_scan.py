#!/usr/bin/env python3
"""Run one validated profile against a bounded list of authorized targets."""

from __future__ import annotations

import argparse
from pathlib import Path

from profile_runner import run_profile
from profiles import PROFILES


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", choices=sorted(PROFILES))
    parser.add_argument("target_file", help="One IP/CIDR/hostname per line; # comments allowed")
    parser.add_argument("--allow-public", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-targets", type=int, default=64, help="Safety cap (default: 64)")
    parser.add_argument("--timing", choices=("T0", "T1", "T2", "T3", "T4"), default="T3")
    args = parser.parse_args()
    if not 1 <= args.max_targets <= 256:
        parser.error("--max-targets must be between 1 and 256")
    try:
        lines = Path(args.target_file).read_text(encoding="utf-8").splitlines()
    except OSError as error:
        parser.error(str(error))
    targets = [line.strip() for line in lines if line.strip() and not line.lstrip().startswith("#")]
    if not targets:
        parser.error("target file contains no targets")
    if len(targets) > args.max_targets:
        parser.error(f"target file has {len(targets)} targets; cap is {args.max_targets}")

    failures = 0
    for index, target in enumerate(targets, start=1):
        print(f"\n[{index}/{len(targets)}] {target}")
        argv = [target, "--timing", args.timing]
        if args.allow_public:
            argv.append("--allow-public")
        if args.dry_run:
            argv.append("--dry-run")
        failures += run_profile(PROFILES[args.profile], argv) != 0
    print(f"\nCompleted: {len(targets) - failures} succeeded; {failures} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
