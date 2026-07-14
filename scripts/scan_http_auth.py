#!/usr/bin/env python3
"""HTTP authentication.

Use case: HTTP authentication: run the installed http-auth NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script http-auth --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_http_auth row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_auth"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
