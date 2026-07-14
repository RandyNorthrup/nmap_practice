#!/usr/bin/env python3
"""HTTP: common application paths.

Use case: Run bounded http-enum NSE checks for common application paths on authorized services.
Core flags: -sT -sV --version-light --script http-enum --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_http_enum row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_enum"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
