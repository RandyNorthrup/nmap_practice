#!/usr/bin/env python3
"""SMB1 security mode.

Use case: SMB1 security mode: run the installed smb-security-mode NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script smb-security-mode --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_smb_security_mode row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_smb_security_mode"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
