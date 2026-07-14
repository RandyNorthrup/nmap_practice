#!/usr/bin/env python3
"""ARP discovery.

Use case: ARP discovery practice profile with bounded Nmap options and saved output.
Core flags: -sn -PR --reason
Risk: low. Scope: private. Raw packets may need elevated privileges.
Modify matching scan_discovery_arp row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discovery_arp"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
