#!/usr/bin/env python3
"""HTTP headers.

Use case: HTTP headers: run the installed http-headers NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script http-headers --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_http_headers row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_headers"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
