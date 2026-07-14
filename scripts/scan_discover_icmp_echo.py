#!/usr/bin/env python3
"""ICMP echo discovery.

Use case: Use ICMP echo requests for discovery.
Core flags: -sn -PE
Risk: low. Scope: private. Raw packets may need elevated privileges.
Modify matching scan_discover_icmp_echo row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discover_icmp_echo"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
