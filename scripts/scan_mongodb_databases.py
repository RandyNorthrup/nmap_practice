#!/usr/bin/env python3
"""MongoDB databases.

Use case: MongoDB databases: run the installed mongodb-databases NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script mongodb-databases --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_mongodb_databases row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_mongodb_databases"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
