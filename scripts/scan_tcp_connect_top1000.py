#!/usr/bin/env python3
"""TCP connect top 1000.

Use case: TCP connect top 1000 practice profile with bounded Nmap options and saved output.
Core flags: -sT --top-ports 1000 --reason --open
Risk: low. Scope: authorized.
Modify matching scan_tcp_connect_top1000 row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_connect_top1000"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
