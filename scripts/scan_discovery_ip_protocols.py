#!/usr/bin/env python3
"""IP protocol discovery.

Use case: IP protocol discovery practice profile with bounded Nmap options and saved output.
Core flags: -sn -PO1,2,4,6,17 --reason
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_discovery_ip_protocols row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discovery_ip_protocols"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
