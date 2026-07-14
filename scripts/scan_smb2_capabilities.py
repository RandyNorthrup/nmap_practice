#!/usr/bin/env python3
"""SMB2 capabilities.

Use case: SMB2 capabilities: run the installed smb2-capabilities NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script smb2-capabilities --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_smb2_capabilities row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_smb2_capabilities"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
