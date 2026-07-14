#!/usr/bin/env python3
"""Discovery NSE suite.

Use case: Discovery NSE suite practice profile with bounded Nmap options and saved output.
Core flags: -sT -sV --version-light --script discovery --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_nse_discovery_profile row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_nse_discovery_profile"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
