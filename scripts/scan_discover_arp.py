#!/usr/bin/env python3
"""ARP discovery.

Use case: Use ARP discovery on local Ethernet.
Core flags: -sn -PR
Risk: low. Scope: private. Raw packets may need elevated privileges.
Modify matching scan_discover_arp row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discover_arp"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
