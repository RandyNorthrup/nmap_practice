#!/usr/bin/env python3
"""Fragmented SYN lab.

Use case: Fragmented SYN lab practice profile with bounded Nmap options and saved output.
Core flags: -sS -f --top-ports 100 --reason
Risk: high. Scope: loopback. Raw packets may need elevated privileges.
Modify matching scan_tcp_fragment_lab row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_fragment_lab"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
