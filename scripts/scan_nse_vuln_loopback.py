#!/usr/bin/env python3
"""Vulnerability NSE loopback.

Use case: Vulnerability NSE loopback practice profile with bounded Nmap options and saved output.
Core flags: -sT -sV --script vuln --script-timeout 60s --open
Risk: high. Scope: loopback.
Modify matching scan_nse_vuln_loopback row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_nse_vuln_loopback"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
