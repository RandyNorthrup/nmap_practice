#!/usr/bin/env python3
"""HTTP: HTML comments.

Use case: Run bounded http-comments-displayer NSE checks for HTML comments on authorized services.
Core flags: -sT -sV --version-light --script http-comments-displayer --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_http_comments_displayer row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_comments_displayer"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
