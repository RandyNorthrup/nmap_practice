#!/usr/bin/env python3
"""Full TCP connect scan.

Use case: Full TCP connect scan practice profile with bounded Nmap options and saved output.
Core flags: -sT -p- --reason --open
Risk: medium. Scope: authorized.
Modify matching scan_tcp_connect_all row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_connect_all"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
