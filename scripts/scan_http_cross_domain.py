#!/usr/bin/env python3
"""Cross-domain policy.

Use case: Cross-domain policy: run the installed http-cross-domain-policy NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script http-cross-domain-policy --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_http_cross_domain row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_cross_domain"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
