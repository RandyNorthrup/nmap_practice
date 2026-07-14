#!/usr/bin/env python3
"""PHP version clues.

Use case: PHP version clues: run the installed http-php-version NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script http-php-version --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_http_php_version row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_php_version"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
