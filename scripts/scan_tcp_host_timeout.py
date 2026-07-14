#!/usr/bin/env python3
"""Bounded TCP scan.

Use case: Bounded TCP scan practice profile with bounded Nmap options and saved output.
Core flags: -sT --top-ports 1000 --host-timeout 30s --reason --open
Risk: low. Scope: authorized.
Modify matching scan_tcp_host_timeout row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_host_timeout"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
