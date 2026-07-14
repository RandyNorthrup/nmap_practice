#!/usr/bin/env python3
"""NTP monitor list.

Use case: NTP monitor list: run the installed ntp-monlist NSE script on expected service ports, with timeout and saved output.
Core flags: -sU -sV --version-light --script ntp-monlist --script-timeout 30s --open
Risk: medium. Scope: private. Raw packets may need elevated privileges.
Modify matching scan_ntp_monlist_private row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ntp_monlist_private"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
