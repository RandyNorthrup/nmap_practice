#!/usr/bin/env python3
"""HTTP methods.

Use case: HTTP methods: run the installed http-methods NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script http-methods --script-timeout 30s --open
Risk: medium. Scope: authorized.
Modify matching scan_http_methods row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_methods"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
