#!/usr/bin/env python3
"""SMB: OS metadata.

Use case: Run bounded smb-os-discovery NSE checks for OS metadata on authorized services.
Core flags: -sT -sV --version-light --script smb-os-discovery --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_smb_os_discovery row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_smb_os_discovery"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
