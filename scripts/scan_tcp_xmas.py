#!/usr/bin/env python3
"""TCP Xmas.

Use case: Compare FIN, PSH, and URG response behavior.
Core flags: -sX
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_tcp_xmas row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_xmas"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
