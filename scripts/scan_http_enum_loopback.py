#!/usr/bin/env python3
"""HTTP path enumeration.

Use case: HTTP path enumeration: run the installed http-enum NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script http-enum --script-timeout 30s --open
Risk: high. Scope: loopback.
Modify matching scan_http_enum_loopback row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_enum_loopback"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
