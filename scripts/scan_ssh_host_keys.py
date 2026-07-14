#!/usr/bin/env python3
"""SSH host keys.

Use case: SSH host keys: run the installed ssh-hostkey NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script ssh-hostkey --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_ssh_host_keys row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ssh_host_keys"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
