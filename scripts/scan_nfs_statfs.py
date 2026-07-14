#!/usr/bin/env python3
"""Infrastructure: NFS filesystem statistics.

Use case: Run bounded nfs-statfs NSE checks for NFS filesystem statistics on authorized services.
Core flags: -sT -sV --version-light --script nfs-statfs --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_nfs_statfs row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_nfs_statfs"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
