#!/usr/bin/env python3
"""TLS Diffie-Hellman parameters.

Use case: TLS Diffie-Hellman parameters: run the installed ssl-dh-params NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script ssl-dh-params --script-timeout 30s --open
Risk: medium. Scope: authorized.
Modify matching scan_tls_dh_params row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tls_dh_params"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
