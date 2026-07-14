#!/usr/bin/env python3
"""Database: MySQL databases.

Use case: Run bounded mysql-databases NSE checks for MySQL databases on authorized services.
Core flags: -sT -sV --version-light --script mysql-databases --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_mysql_databases row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_mysql_databases"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
