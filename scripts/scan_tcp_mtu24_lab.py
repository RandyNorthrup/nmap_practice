#!/usr/bin/env python3
"""Custom MTU SYN lab.

Use case: Custom MTU SYN lab practice profile with bounded Nmap options and saved output.
Core flags: -sS --mtu 24 --top-ports 100 --reason
Risk: high. Scope: loopback. Raw packets may need elevated privileges.
Modify matching scan_tcp_mtu24_lab row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_mtu24_lab"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
