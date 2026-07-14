#!/usr/bin/env python3
"""Infrastructure: RDP encryption.

Use case: Run bounded rdp-enum-encryption NSE checks for RDP encryption on authorized services.
Core flags: -sT -sV --version-light --script rdp-enum-encryption --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_rdp_enum_encryption row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_rdp_enum_encryption"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
