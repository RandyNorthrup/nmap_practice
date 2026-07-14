#!/usr/bin/env python3
"""IPv6 host discovery.

Use case: IPv6 host discovery practice profile with bounded Nmap options and saved output.
Core flags: -6 -sn --reason
Risk: low. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_discovery_ipv6 row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discovery_ipv6"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
