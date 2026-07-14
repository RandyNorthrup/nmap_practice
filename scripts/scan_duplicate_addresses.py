#!/usr/bin/env python3
"""Duplicate address check.

Use case: Duplicate address check: run the installed duplicates NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script duplicates --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_duplicate_addresses row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_duplicate_addresses"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
