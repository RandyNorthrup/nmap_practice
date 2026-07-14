#!/usr/bin/env python3
"""TCP NULL.

Use case: Compare TCP packets with no flags set.
Core flags: -sN
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_tcp_null row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_null"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
