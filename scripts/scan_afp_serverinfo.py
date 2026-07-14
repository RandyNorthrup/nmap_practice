#!/usr/bin/env python3
"""Infrastructure: AFP information.

Use case: Run bounded afp-serverinfo NSE checks for AFP information on authorized services.
Core flags: -sT -sV --version-light --script afp-serverinfo --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_afp_serverinfo row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_afp_serverinfo"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
