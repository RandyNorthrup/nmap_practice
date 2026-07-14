#!/usr/bin/env python3
"""Intrusive NSE loopback.

Use case: Intrusive NSE loopback practice profile with bounded Nmap options and saved output.
Core flags: -sT -sV --script intrusive --script-timeout 60s --open
Risk: high. Scope: loopback.
Modify matching scan_nse_intrusive_loopback row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_nse_intrusive_loopback"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
