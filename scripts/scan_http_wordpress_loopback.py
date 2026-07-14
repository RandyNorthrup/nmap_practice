#!/usr/bin/env python3
"""WordPress enumeration.

Use case: WordPress enumeration: run the installed http-wordpress-enum NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script http-wordpress-enum --script-timeout 30s --open
Risk: high. Scope: loopback.
Modify matching scan_http_wordpress_loopback row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_wordpress_loopback"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
