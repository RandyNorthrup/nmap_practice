#!/usr/bin/env python3
"""Common UDP.

Use case: Scan DNS, NTP, SNMP, IKE, and lab UDP ports.
Core flags: -sU
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_udp_common row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_udp_common"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
