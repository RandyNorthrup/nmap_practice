#!/usr/bin/env python3
"""Database: MSSQL instances.

Use case: Run bounded ms-sql-info NSE checks for MSSQL instances on authorized services.
Core flags: -sT -sV --version-light --script ms-sql-info --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_ms_sql_info row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ms_sql_info"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
