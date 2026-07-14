#!/usr/bin/env python3
"""HTTP robots file.

Use case: HTTP robots file: run the installed http-robots.txt NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script http-robots.txt --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_http_robots row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_robots"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
