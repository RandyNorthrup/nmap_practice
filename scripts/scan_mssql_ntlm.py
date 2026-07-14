#!/usr/bin/env python3
"""Microsoft SQL NTLM metadata.

Use case: Microsoft SQL NTLM metadata: run the installed ms-sql-ntlm-info NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script ms-sql-ntlm-info --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_mssql_ntlm row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_mssql_ntlm"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
