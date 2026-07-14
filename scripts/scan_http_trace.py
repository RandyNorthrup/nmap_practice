#!/usr/bin/env python3
"""HTTP: TRACE behavior.

Use case: Run bounded http-trace NSE checks for TRACE behavior on authorized services.
Core flags: -sT -sV --version-light --script http-trace --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_http_trace row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_trace"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
