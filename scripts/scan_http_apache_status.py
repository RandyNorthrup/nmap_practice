#!/usr/bin/env python3
"""Apache status page.

Use case: Apache status page: run the installed http-apache-server-status NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script http-apache-server-status --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_http_apache_status row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_apache_status"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
