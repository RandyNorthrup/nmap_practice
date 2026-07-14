#!/usr/bin/env python3
"""Finger service.

Use case: Finger service: run the installed finger NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script finger --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_finger_info row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_finger_info"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
