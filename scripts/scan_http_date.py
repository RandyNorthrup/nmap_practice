#!/usr/bin/env python3
"""HTTP server date.

Use case: HTTP server date: run the installed http-date NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script http-date --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_http_date row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_date"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
