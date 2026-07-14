#!/usr/bin/env python3
"""SSH: protocol algorithms.

Use case: Run bounded ssh2-enum-algos NSE checks for protocol algorithms on authorized services.
Core flags: -sT -sV --version-light --script ssh2-enum-algos --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_ssh2_enum_algos row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ssh2_enum_algos"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
