#!/usr/bin/env python3
"""BIG-IP cookie metadata.

Use case: BIG-IP cookie metadata: run the installed http-bigip-cookie NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script http-bigip-cookie --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_http_bigip_cookie row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_bigip_cookie"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
