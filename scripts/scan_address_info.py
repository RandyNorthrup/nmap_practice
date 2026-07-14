#!/usr/bin/env python3
"""Address metadata.

Use case: Address metadata: run the installed address-info NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script address-info --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_address_info row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_address_info"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
