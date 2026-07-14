#!/usr/bin/env python3
"""IPv6 discovery.

Use case: Run default host discovery over IPv6.
Core flags: -6 -sn
Risk: low. Scope: authorized.
Modify matching scan_discover_ipv6 row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discover_ipv6"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
