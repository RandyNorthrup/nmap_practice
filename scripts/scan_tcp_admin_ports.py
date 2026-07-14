#!/usr/bin/env python3
"""Administration ports.

Use case: Scan common remote administration ports.
Core flags: -sT
Risk: low. Scope: authorized.
Modify matching scan_tcp_admin_ports row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_admin_ports"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
