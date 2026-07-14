#!/usr/bin/env python3
"""Clock-skew inspection.

Use case: Clock-skew inspection: run the installed clock-skew NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script clock-skew --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_clock_skew row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_clock_skew"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
