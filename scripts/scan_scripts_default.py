#!/usr/bin/env python3
"""Default NSE.

Use case: Run Nmap default NSE scripts.
Core flags: -sT -sV --script default --top-ports 100
Risk: medium. Scope: authorized.
Modify matching scan_scripts_default row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_scripts_default"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
