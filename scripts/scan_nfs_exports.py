#!/usr/bin/env python3
"""NFS exports.

Use case: NFS exports: run the installed nfs-showmount NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script nfs-showmount --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_nfs_exports row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_nfs_exports"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
