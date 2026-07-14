#!/usr/bin/env python3
"""MySQL empty password.

Use case: MySQL empty password: run the installed mysql-empty-password NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script mysql-empty-password --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_mysql_empty_password row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_mysql_empty_password"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
