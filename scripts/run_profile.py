#!/usr/bin/env python3
"""Run any named profile without finding its dedicated entry script."""

from __future__ import annotations

import sys

from profile_runner import run_named_profile
from profiles import PROFILES


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] in {"-h", "--help"}:
        print("Usage: run_profile.py PROFILE TARGET [OPTIONS]")
        print(f"Profiles available: {len(PROFILES)}")
        print("Search them with: python scripts/catalog.py QUERY")
        return 0
    name = sys.argv.pop(1)
    if name not in PROFILES:
        print(f"Error: unknown profile {name!r}. Search with catalog.py.", file=sys.stderr)
        return 2
    return run_named_profile(name)


if __name__ == "__main__":
    raise SystemExit(main())
