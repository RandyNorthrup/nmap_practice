#!/usr/bin/env python3
"""Database: Oracle TNS version.

Use case: Run bounded oracle-tns-version NSE checks for Oracle TNS version on authorized services.
Core flags: -sT -sV --version-light --script oracle-tns-version --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_oracle_tns_version row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_oracle_tns_version"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
