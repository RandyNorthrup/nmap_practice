#!/usr/bin/env python3
"""Sequential TCP ports.

Use case: Sequential TCP ports practice profile with bounded Nmap options and saved output.
Core flags: -sT --top-ports 100 -r --reason --open
Risk: low. Scope: authorized.
Modify matching scan_tcp_sequential row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_sequential"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
