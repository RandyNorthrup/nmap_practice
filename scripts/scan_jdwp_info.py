#!/usr/bin/env python3
"""Infrastructure: JDWP information.

Use case: Run bounded jdwp-info NSE checks for JDWP information on authorized services.
Core flags: -sT -sV --version-light --script jdwp-info --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_jdwp_info row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_jdwp_info"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
