#!/usr/bin/env python3
"""DNS service discovery.

Use case: DNS service discovery: run the installed dns-service-discovery NSE script on expected service ports, with timeout and saved output.
Core flags: -sU -sV --version-light --script dns-service-discovery --script-timeout 30s --open
Risk: low. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_dns_service_discovery row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_dns_service_discovery"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
