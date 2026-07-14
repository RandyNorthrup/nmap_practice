#!/usr/bin/env python3
"""TLS cipher suites.

Use case: TLS cipher suites: run the installed ssl-enum-ciphers NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script ssl-enum-ciphers --script-timeout 30s --open
Risk: medium. Scope: authorized.
Modify matching scan_tls_ciphers row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tls_ciphers"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
