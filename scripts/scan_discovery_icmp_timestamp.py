#!/usr/bin/env python3
"""ICMP timestamp discovery.

Use case: ICMP timestamp discovery practice profile with bounded Nmap options and saved output.
Core flags: -sn -PP --reason
Risk: low. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_discovery_icmp_timestamp row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discovery_icmp_timestamp"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
