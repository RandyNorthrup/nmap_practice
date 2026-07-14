#!/usr/bin/env python3
"""Aggressive OS guessing.

Use case: Aggressive OS guessing practice profile with bounded Nmap options and saved output.
Core flags: -O --osscan-guess --top-ports 1000 --reason
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_os_guess_profile row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_os_guess_profile"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
