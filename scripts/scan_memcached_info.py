#!/usr/bin/env python3
"""Memcached information.

Use case: Memcached information: run the installed memcached-info NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script memcached-info --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_memcached_info row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_memcached_info"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
