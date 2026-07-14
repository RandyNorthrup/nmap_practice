#!/usr/bin/env python3
"""SMB2 server time.

Use case: SMB2 server time: run the installed smb2-time NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script smb2-time --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_smb2_time row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_smb2_time"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
