#!/usr/bin/env python3
"""Generic banners.

Use case: Collect generic banners from selected services.
Core flags: -sT -sV --script banner
Risk: low. Scope: authorized.
Modify matching scan_service_banner row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_service_banner"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
