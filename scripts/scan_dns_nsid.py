#!/usr/bin/env python3
"""DNS server identity.

Use case: DNS server identity: run the installed dns-nsid NSE script on expected service ports, with timeout and saved output.
Core flags: -sU -sV --version-light --script dns-nsid --script-timeout 30s --open
Risk: low. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_dns_nsid row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_dns_nsid"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
