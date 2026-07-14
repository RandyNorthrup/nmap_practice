#!/usr/bin/env python3
"""TCP scan without discovery.

Use case: TCP scan without discovery practice profile with bounded Nmap options and saved output.
Core flags: -Pn -sT --top-ports 100 --reason --open
Risk: low. Scope: authorized.
Modify matching scan_tcp_without_discovery row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_without_discovery"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
