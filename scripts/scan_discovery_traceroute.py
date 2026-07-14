#!/usr/bin/env python3
"""Discovery with traceroute.

Use case: Discovery with traceroute practice profile with bounded Nmap options and saved output.
Core flags: -sn --traceroute --reason
Risk: low. Scope: authorized.
Modify matching scan_discovery_traceroute row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discovery_traceroute"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
