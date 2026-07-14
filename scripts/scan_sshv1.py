#!/usr/bin/env python3
"""SSH: obsolete protocol v1 support.

Use case: Run bounded sshv1 NSE checks for obsolete protocol v1 support on authorized services.
Core flags: -sT -sV --version-light --script sshv1 --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_sshv1 row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_sshv1"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
