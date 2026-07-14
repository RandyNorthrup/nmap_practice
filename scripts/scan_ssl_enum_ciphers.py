#!/usr/bin/env python3
"""TLS: versions and ciphers.

Use case: Run bounded ssl-enum-ciphers NSE checks for versions and ciphers on authorized services.
Core flags: -sT -sV --version-light --script ssl-enum-ciphers --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_ssl_enum_ciphers row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ssl_enum_ciphers"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
