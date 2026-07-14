#!/usr/bin/env python3
"""JSONP endpoint detection.

Use case: JSONP endpoint detection: run the installed http-jsonp-detection NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script http-jsonp-detection --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_http_jsonp row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_jsonp"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
