#!/usr/bin/env python3
"""TLS: internal certificate addresses.

Use case: Run bounded ssl-cert-intaddr NSE checks for internal certificate addresses on authorized services.
Core flags: -sT -sV --version-light --script ssl-cert-intaddr --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_ssl_cert_intaddr row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ssl_cert_intaddr"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
