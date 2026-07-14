#!/usr/bin/env python3
"""TLS: ALPN protocols.

Use case: Run bounded tls-alpn NSE checks for ALPN protocols on authorized services.
Core flags: -sT -sV --version-light --script tls-alpn --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_tls_alpn row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tls_alpn"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
