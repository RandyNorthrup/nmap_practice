#!/usr/bin/env python3
"""NFS directory listing.

Use case: NFS directory listing: run the installed nfs-ls NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script nfs-ls --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_nfs_listing row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_nfs_listing"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
