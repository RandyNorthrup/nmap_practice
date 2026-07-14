#!/usr/bin/env python3
"""DNS SRV records.

Use case: DNS SRV records: run the installed dns-srv-enum NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script dns-srv-enum --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_dns_srv_records row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_dns_srv_records"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
