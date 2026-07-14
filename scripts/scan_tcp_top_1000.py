#!/usr/bin/env python3
"""Top 1000 TCP.

Use case: TCP connect scan of 1000 common ports.
Core flags: -sT --top-ports 1000
Risk: medium. Scope: authorized.
Modify matching scan_tcp_top_1000 row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_top_1000"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
