#!/usr/bin/env python3
"""Infrastructure: NFS export contents.

Use case: Run bounded nfs-ls NSE checks for NFS export contents on authorized services.
Core flags: -sT -sV --version-light --script nfs-ls --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_nfs_ls row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_nfs_ls"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
