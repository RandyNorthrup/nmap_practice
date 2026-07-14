#!/usr/bin/env python3
"""HTTP cookie flags.

Use case: HTTP cookie flags: run the installed http-cookie-flags NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script http-cookie-flags --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_http_cookie_flags row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_cookie_flags"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
