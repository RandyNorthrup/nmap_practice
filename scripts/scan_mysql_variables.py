#!/usr/bin/env python3
"""MySQL variables.

Use case: MySQL variables: run the installed mysql-variables NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script mysql-variables --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_mysql_variables row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_mysql_variables"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
