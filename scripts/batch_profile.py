#!/usr/bin/env python3
"""Run one validated scan profile against targets from a text file sequentially."""

from __future__ import annotations

import argparse
from pathlib import Path
import re

from profile_runner import run_profile
from profiles import PROFILES


def safe_name(target: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]", "_", target)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", help="Profile name; use profile_catalog.py")
    parser.add_argument("targets", help="Text file: one target/CIDR per line; # comments allowed")
    parser.add_argument("--output-dir", default="results/batch")
    parser.add_argument("--allow-public", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--continue-on-error", action="store_true")
    args = parser.parse_args()
    item = PROFILES.get(args.profile)
    if item is None:
        parser.error(f"Unknown profile: {args.profile}")
    try:
        lines = Path(args.targets).read_text(encoding="utf-8").splitlines()
    except OSError as error:
        parser.error(str(error))
    targets = [line.split("#", 1)[0].strip() for line in lines]
    targets = [target for target in targets if target]
    if not targets:
        parser.error("Target file contains no targets")

    failures = 0
    for index, target in enumerate(targets, start=1):
        output = Path(args.output_dir) / f"{index:03d}-{safe_name(target)}"
        argv = [target, "--output", str(output)]
        if args.allow_public:
            argv.append("--allow-public")
        if args.dry_run:
            argv.append("--dry-run")
        code = run_profile(item, argv)
        if code:
            failures += 1
            if not args.continue_on_error:
                return code
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
