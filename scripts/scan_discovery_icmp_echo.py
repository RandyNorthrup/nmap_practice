#!/usr/bin/env python3
"""ICMP echo discovery.

Use case: ICMP echo discovery practice profile with bounded Nmap options and saved output.
Core flags: -sn -PE --reason
Risk: low. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_discovery_icmp_echo row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discovery_icmp_echo"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
