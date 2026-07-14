#!/usr/bin/env python3
"""FTP: bounce behavior.

Use case: Run bounded ftp-bounce NSE checks for bounce behavior on authorized services.
Core flags: -sT -sV --version-light --script ftp-bounce --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_ftp_bounce row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ftp_bounce"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
