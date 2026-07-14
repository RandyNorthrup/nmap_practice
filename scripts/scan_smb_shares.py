#!/usr/bin/env python3
"""SMB shares.

Use case: SMB shares: run the installed smb-enum-shares NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script smb-enum-shares --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_smb_shares row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_smb_shares"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
