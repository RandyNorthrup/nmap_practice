#!/usr/bin/env python3
"""IP protocol discovery.

Use case: Discover hosts using selected IP protocols.
Core flags: -sn -PO1,2,4
Risk: low. Scope: private. Raw packets may need elevated privileges.
Modify matching scan_discover_ip_protocol row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discover_ip_protocol"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
