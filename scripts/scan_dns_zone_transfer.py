#!/usr/bin/env python3
"""DNS zone transfer.

Use case: DNS zone transfer: run the installed dns-zone-transfer NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script dns-zone-transfer --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_dns_zone_transfer row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_dns_zone_transfer"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
