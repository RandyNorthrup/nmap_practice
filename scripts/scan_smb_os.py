#!/usr/bin/env python3
"""SMB OS discovery.

Use case: SMB OS discovery: run the installed smb-os-discovery NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script smb-os-discovery --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_smb_os row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_smb_os"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
