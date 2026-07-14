#!/usr/bin/env python3
"""HTTP: robots rules.

Use case: Run bounded http-robots.txt NSE checks for robots rules on authorized services.
Core flags: -sT -sV --version-light --script http-robots.txt --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_http_robots_txt row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_robots_txt"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
