#!/usr/bin/env python3
"""HTTP title.

Use case: HTTP title: run the installed http-title NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script http-title --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_http_title row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_title"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
