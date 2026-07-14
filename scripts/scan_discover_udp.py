#!/usr/bin/env python3
"""UDP discovery.

Use case: Discover hosts with narrow DNS, NTP, and SNMP probes.
Core flags: -sn -PU53,123,161
Risk: low. Scope: private. Raw packets may need elevated privileges.
Modify matching scan_discover_udp row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discover_udp"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
