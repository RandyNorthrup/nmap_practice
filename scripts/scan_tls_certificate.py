#!/usr/bin/env python3
"""TLS certificate.

Use case: TLS certificate: run the installed ssl-cert NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script ssl-cert --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_tls_certificate row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tls_certificate"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
