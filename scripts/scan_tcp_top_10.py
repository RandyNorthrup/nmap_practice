#!/usr/bin/env python3
"""Top 10 TCP.

Use case: TCP connect scan of ten common ports.
Core flags: -sT --top-ports 10
Risk: low. Scope: authorized.
Modify matching scan_tcp_top_10 row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_top_10"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
