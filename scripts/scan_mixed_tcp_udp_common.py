#!/usr/bin/env python3
"""Mixed TCP and UDP.

Use case: Mixed TCP and UDP practice profile with bounded Nmap options and saved output.
Core flags: -sS -sU --reason --open
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_mixed_tcp_udp_common row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_mixed_tcp_udp_common"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
