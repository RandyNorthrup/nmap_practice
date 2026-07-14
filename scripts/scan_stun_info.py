#!/usr/bin/env python3
"""Infrastructure: STUN information.

Use case: Run bounded stun-info NSE checks for STUN information on authorized services.
Core flags: -sU -sV --version-light --script stun-info --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_stun_info row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_stun_info"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
