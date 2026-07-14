#!/usr/bin/env python3
"""Default host discovery.

Use case: Default host discovery practice profile with bounded Nmap options and saved output.
Core flags: -sn --reason
Risk: low. Scope: authorized.
Modify matching scan_discovery_default_profile row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discovery_default_profile"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
