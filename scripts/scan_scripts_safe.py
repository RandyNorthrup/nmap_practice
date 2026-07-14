#!/usr/bin/env python3
"""Safe NSE.

Use case: Run NSE scripts categorized safe.
Core flags: -sT -sV --script safe --top-ports 100
Risk: medium. Scope: authorized.
Modify matching scan_scripts_safe row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_scripts_safe"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
