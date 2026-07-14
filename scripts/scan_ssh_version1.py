#!/usr/bin/env python3
"""SSH version 1 support.

Use case: SSH version 1 support: run the installed sshv1 NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script sshv1 --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_ssh_version1 row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ssh_version1"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
