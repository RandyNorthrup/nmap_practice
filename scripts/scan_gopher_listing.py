#!/usr/bin/env python3
"""Gopher listing.

Use case: Gopher listing: run the installed gopher-ls NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script gopher-ls --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_gopher_listing row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_gopher_listing"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
