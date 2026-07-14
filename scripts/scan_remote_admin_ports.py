#!/usr/bin/env python3
"""Remote administration ports.

Use case: Inventory remote administration ports with TCP connect and light service detection.
Core flags: -sT -sV --version-light --reason --open
Risk: low. Scope: authorized.
Modify matching scan_remote_admin_ports row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_remote_admin_ports"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
