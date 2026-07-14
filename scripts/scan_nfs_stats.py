#!/usr/bin/env python3
"""NFS filesystem stats.

Use case: NFS filesystem stats: run the installed nfs-statfs NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script nfs-statfs --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_nfs_stats row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_nfs_stats"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
