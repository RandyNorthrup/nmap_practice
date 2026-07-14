#!/usr/bin/env python3
"""TLS: DH parameters.

Use case: Run bounded ssl-dh-params NSE checks for DH parameters on authorized services.
Core flags: -sT -sV --version-light --script ssl-dh-params --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_ssl_dh_params row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ssl_dh_params"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
