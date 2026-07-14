#!/usr/bin/env python3
"""Generic banner collection.

Use case: Generic banner collection practice profile with bounded Nmap options and saved output.
Core flags: -sT -sV --version-light --script banner --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_banner_grab row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_banner_grab"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
