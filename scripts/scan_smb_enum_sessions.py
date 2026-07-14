#!/usr/bin/env python3
"""SMB: sessions.

Use case: Run bounded smb-enum-sessions NSE checks for sessions on authorized services.
Core flags: -sT -sV --version-light --script smb-enum-sessions --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_smb_enum_sessions row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_smb_enum_sessions"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
