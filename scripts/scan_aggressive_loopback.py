#!/usr/bin/env python3
"""Aggressive loopback profile.

Use case: Aggressive loopback profile practice profile with bounded Nmap options and saved output.
Core flags: -A --reason
Risk: high. Scope: loopback. Raw packets may need elevated privileges.
Modify matching scan_aggressive_loopback row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_aggressive_loopback"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
