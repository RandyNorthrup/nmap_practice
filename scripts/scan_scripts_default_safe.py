#!/usr/bin/env python3
"""Default and safe NSE.

Use case: Run scripts in both default and safe sets.
Core flags: -sT -sV --script default and safe --top-ports 100
Risk: low. Scope: authorized.
Modify matching scan_scripts_default_safe row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_scripts_default_safe"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
