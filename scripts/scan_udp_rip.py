#!/usr/bin/env python3
"""UDP routing protocols.

Use case: UDP routing protocols practice profile with bounded Nmap options and saved output.
Core flags: -sU --reason --open
Risk: medium. Scope: private. Raw packets may need elevated privileges.
Modify matching scan_udp_rip row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_udp_rip"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
