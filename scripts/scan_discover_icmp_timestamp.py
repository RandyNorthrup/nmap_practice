#!/usr/bin/env python3
"""ICMP timestamp discovery.

Use case: Use ICMP timestamp requests for discovery.
Core flags: -sn -PP
Risk: low. Scope: private. Raw packets may need elevated privileges.
Modify matching scan_discover_icmp_timestamp row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discover_icmp_timestamp"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
