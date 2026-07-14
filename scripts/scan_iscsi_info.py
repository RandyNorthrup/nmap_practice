#!/usr/bin/env python3
"""Infrastructure: iSCSI target information.

Use case: Run bounded iscsi-info NSE checks for iSCSI target information on authorized services.
Core flags: -sT -sV --version-light --script iscsi-info --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_iscsi_info row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_iscsi_info"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
