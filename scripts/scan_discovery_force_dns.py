#!/usr/bin/env python3
"""Host discovery with DNS.

Use case: Host discovery with DNS practice profile with bounded Nmap options and saved output.
Core flags: -sn -R --reason
Risk: low. Scope: authorized.
Modify matching scan_discovery_force_dns row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discovery_force_dns"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
