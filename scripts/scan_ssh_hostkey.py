#!/usr/bin/env python3
"""SSH: host-key fingerprints.

Use case: Run bounded ssh-hostkey NSE checks for host-key fingerprints on authorized services.
Core flags: -sT -sV --version-light --script ssh-hostkey --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_ssh_hostkey row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ssh_hostkey"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
