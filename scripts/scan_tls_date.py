#!/usr/bin/env python3
"""TLS server date.

Use case: TLS server date: run the installed ssl-date NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script ssl-date --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_tls_date row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tls_date"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
