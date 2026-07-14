#!/usr/bin/env python3
"""Infrastructure: Siemens S7 information.

Use case: Run bounded s7-info NSE checks for Siemens S7 information on authorized services.
Core flags: -sT -sV --version-light --script s7-info --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_s7_info row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_s7_info"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
