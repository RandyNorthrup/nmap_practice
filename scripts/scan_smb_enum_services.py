#!/usr/bin/env python3
"""SMB: services.

Use case: Run bounded smb-enum-services NSE checks for services on authorized services.
Core flags: -sT -sV --version-light --script smb-enum-services --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_smb_enum_services row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_smb_enum_services"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
