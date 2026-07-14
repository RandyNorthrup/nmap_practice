#!/usr/bin/env python3
"""SMB users.

Use case: SMB users: run the installed smb-enum-users NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script smb-enum-users --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_smb_users row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_smb_users"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
