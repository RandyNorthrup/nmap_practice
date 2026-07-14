#!/usr/bin/env python3
"""TLS: certificate details.

Use case: Run bounded ssl-cert NSE checks for certificate details on authorized services.
Core flags: -sT -sV --version-light --script ssl-cert --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_ssl_cert row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ssl_cert"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
