#!/usr/bin/env python3
"""Safe NSE suite.

Use case: Safe NSE suite practice profile with bounded Nmap options and saved output.
Core flags: -sT -sV --version-light --script default and safe --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_nse_safe_profile row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_nse_safe_profile"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
