#!/usr/bin/env python3
"""Database ports.

Use case: Scan common database and cache ports.
Core flags: -sT
Risk: low. Scope: authorized.
Modify matching scan_tcp_database_ports row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_database_ports"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
