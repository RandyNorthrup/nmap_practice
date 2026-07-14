#!/usr/bin/env python3
"""DNS recursion.

Use case: DNS recursion: run the installed dns-recursion NSE script on expected service ports, with timeout and saved output.
Core flags: -sU -sV --version-light --script dns-recursion --script-timeout 30s --open
Risk: low. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_dns_recursion row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_dns_recursion"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
