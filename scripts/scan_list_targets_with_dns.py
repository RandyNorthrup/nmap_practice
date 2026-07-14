#!/usr/bin/env python3
"""List targets with DNS.

Use case: List targets with DNS practice profile with bounded Nmap options and saved output.
Core flags: -sL -R
Risk: low. Scope: authorized.
Modify matching scan_list_targets_with_dns row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_list_targets_with_dns"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
