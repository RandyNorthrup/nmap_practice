#!/usr/bin/env python3
"""HTTP comments.

Use case: HTTP comments: run the installed http-comments-displayer NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script http-comments-displayer --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_http_comments row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_comments"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
