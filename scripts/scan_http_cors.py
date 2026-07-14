#!/usr/bin/env python3
"""HTTP CORS policy.

Use case: HTTP CORS policy: run the installed http-cors NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script http-cors --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_http_cors row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_cors"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
