#!/usr/bin/env python3
"""UDP DHCP ports.

Use case: UDP DHCP ports practice profile with bounded Nmap options and saved output.
Core flags: -sU --reason --open
Risk: medium. Scope: private. Raw packets may need elevated privileges.
Modify matching scan_udp_dhcp row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_udp_dhcp"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
