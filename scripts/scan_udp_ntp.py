#!/usr/bin/env python3
"""UDP NTP.

Use case: UDP NTP practice profile with bounded Nmap options and saved output.
Core flags: -sU --reason --open
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_udp_ntp row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_udp_ntp"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
