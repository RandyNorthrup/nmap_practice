#!/usr/bin/env python3
"""SSH authentication methods.

Use case: SSH authentication methods: run the installed ssh-auth-methods NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script ssh-auth-methods --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_ssh_auth_methods row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ssh_auth_methods"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
