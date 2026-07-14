#!/usr/bin/env python3
"""TCP connect.

Use case: Use operating-system TCP connect calls.
Core flags: -sT
Risk: low. Scope: authorized.
Modify matching scan_tcp_connect row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_connect"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
