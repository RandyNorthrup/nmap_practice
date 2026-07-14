#!/usr/bin/env python3
"""FTP: anonymous access.

Use case: Run bounded ftp-anon NSE checks for anonymous access on authorized services.
Core flags: -sT -sV --version-light --script ftp-anon --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_ftp_anon row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ftp_anon"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
