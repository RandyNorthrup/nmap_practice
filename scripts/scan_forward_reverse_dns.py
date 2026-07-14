#!/usr/bin/env python3
"""Forward-confirmed reverse DNS.

Use case: Forward-confirmed reverse DNS: run the installed fcrdns NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script fcrdns --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_forward_reverse_dns row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_forward_reverse_dns"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
