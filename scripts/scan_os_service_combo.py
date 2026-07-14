#!/usr/bin/env python3
"""OS and service inventory.

Use case: OS and service inventory practice profile with bounded Nmap options and saved output.
Core flags: -O -sV --version-light --top-ports 1000 --reason --open
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_os_service_combo row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_os_service_combo"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
