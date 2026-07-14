#!/usr/bin/env python3
"""Mixed TCP and UDP.

Use case: Scan a small combined TCP and UDP set.
Core flags: -sT -sU -p T:22,80,443,U:53,123,161
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_mixed_tcp_udp row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_mixed_tcp_udp"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
