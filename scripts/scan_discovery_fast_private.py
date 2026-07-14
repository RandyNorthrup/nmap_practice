#!/usr/bin/env python3
"""Faster private discovery.

Use case: Faster private discovery practice profile with bounded Nmap options and saved output.
Core flags: -sn --reason
Risk: medium. Scope: private.
Modify matching scan_discovery_fast_private row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discovery_fast_private"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
