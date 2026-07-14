#!/usr/bin/env python3
"""DNS: source-port randomization.

Use case: Run bounded dns-random-srcport NSE checks for source-port randomization on authorized services.
Core flags: -sU -sV --version-light --script dns-random-srcport --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_dns_random_srcport row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_dns_random_srcport"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
