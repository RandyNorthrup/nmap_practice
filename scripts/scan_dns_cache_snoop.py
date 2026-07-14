#!/usr/bin/env python3
"""DNS: cache behavior.

Use case: Run bounded dns-cache-snoop NSE checks for cache behavior on authorized services.
Core flags: -sU -sV --version-light --script dns-cache-snoop --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_dns_cache_snoop row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_dns_cache_snoop"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
