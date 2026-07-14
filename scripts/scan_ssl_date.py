#!/usr/bin/env python3
"""TLS: service clock.

Use case: Run bounded ssl-date NSE checks for service clock on authorized services.
Core flags: -sT -sV --version-light --script ssl-date --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_ssl_date row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ssl_date"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
