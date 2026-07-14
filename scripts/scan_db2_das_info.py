#!/usr/bin/env python3
"""Database: DB2 information.

Use case: Run bounded db2-das-info NSE checks for DB2 information on authorized services.
Core flags: -sT -sV --version-light --script db2-das-info --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_db2_das_info row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_db2_das_info"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
