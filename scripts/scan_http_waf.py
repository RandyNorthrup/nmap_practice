#!/usr/bin/env python3
"""Web application firewall detection.

Use case: Web application firewall detection: run the installed http-waf-detect NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script http-waf-detect --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_http_waf row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_waf"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
