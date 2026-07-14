#!/usr/bin/env python3
"""Full UDP loopback scan.

Use case: Full UDP loopback scan practice profile with bounded Nmap options and saved output.
Core flags: -sU -p- --reason --open
Risk: high. Scope: loopback. Raw packets may need elevated privileges.
Modify matching scan_udp_all_lab row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_udp_all_lab"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
