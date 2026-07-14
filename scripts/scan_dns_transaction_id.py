#!/usr/bin/env python3
"""DNS transaction-ID randomness.

Use case: DNS transaction-ID randomness: run the installed dns-random-txid NSE script on expected service ports, with timeout and saved output.
Core flags: -sU -sV --version-light --script dns-random-txid --script-timeout 30s --open
Risk: low. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_dns_transaction_id row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_dns_transaction_id"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
