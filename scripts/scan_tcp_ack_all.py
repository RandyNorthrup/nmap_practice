#!/usr/bin/env python3
"""Full TCP ACK firewall map.

Use case: Full TCP ACK firewall map practice profile with bounded Nmap options and saved output.
Core flags: -sA -p- --reason
Risk: high. Scope: private. Raw packets may need elevated privileges.
Modify matching scan_tcp_ack_all row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_ack_all"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
