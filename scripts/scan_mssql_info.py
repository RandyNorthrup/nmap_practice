#!/usr/bin/env python3
"""Microsoft SQL information.

Use case: Microsoft SQL information: run the installed ms-sql-info NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script ms-sql-info --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_mssql_info row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_mssql_info"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
