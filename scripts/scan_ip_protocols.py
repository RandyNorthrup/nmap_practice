#!/usr/bin/env python3
"""IP protocol scan.

Use case: IP protocol scan practice profile with bounded Nmap options and saved output.
Core flags: -sO --reason
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_ip_protocols row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ip_protocols"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
