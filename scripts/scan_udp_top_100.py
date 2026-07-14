#!/usr/bin/env python3
"""Top 100 UDP.

Use case: Scan 100 most common UDP ports.
Core flags: -sU --top-ports 100
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_udp_top_100 row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_udp_top_100"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
