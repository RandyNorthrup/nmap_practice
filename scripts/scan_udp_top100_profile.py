#!/usr/bin/env python3
"""UDP top 100.

Use case: UDP top 100 practice profile with bounded Nmap options and saved output.
Core flags: -sU --top-ports 100 --reason --open
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_udp_top100_profile row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_udp_top100_profile"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
