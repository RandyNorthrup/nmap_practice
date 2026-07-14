#!/usr/bin/env python3
"""DNS: transaction-ID randomization.

Use case: Run bounded dns-random-txid NSE checks for transaction-ID randomization on authorized services.
Core flags: -sU -sV --version-light --script dns-random-txid --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_dns_random_txid row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_dns_random_txid"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
