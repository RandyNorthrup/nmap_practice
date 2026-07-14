#!/usr/bin/env python3
"""NTP information.

Use case: NTP information: run the installed ntp-info NSE script on expected service ports, with timeout and saved output.
Core flags: -sU -sV --version-light --script ntp-info --script-timeout 30s --open
Risk: low. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_ntp_info row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ntp_info"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
