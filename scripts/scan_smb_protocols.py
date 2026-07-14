#!/usr/bin/env python3
"""SMB protocols.

Use case: SMB protocols: run the installed smb-protocols NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script smb-protocols --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_smb_protocols row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_smb_protocols"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
