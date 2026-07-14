#!/usr/bin/env python3
"""TCP Xmas scan.

Use case: TCP Xmas scan practice profile with bounded Nmap options and saved output.
Core flags: -sX --top-ports 100 --reason
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_tcp_xmas_common row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_xmas_common"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
