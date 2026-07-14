#!/usr/bin/env python3
"""TLS: known-key matches.

Use case: Run bounded ssl-known-key NSE checks for known-key matches on authorized services.
Core flags: -sT -sV --version-light --script ssl-known-key --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_ssl_known_key row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ssl_known_key"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
