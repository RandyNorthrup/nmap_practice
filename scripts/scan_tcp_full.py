#!/usr/bin/env python3
"""Full TCP.

Use case: Scan all 65535 TCP ports on one authorized host.
Core flags: -sT -p-
Risk: medium. Scope: authorized.
Modify matching scan_tcp_full row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_full"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
