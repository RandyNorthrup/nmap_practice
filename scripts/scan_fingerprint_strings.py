#!/usr/bin/env python3
"""Unknown service strings.

Use case: Unknown service strings: run the installed fingerprint-strings NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script fingerprint-strings --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_fingerprint_strings row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_fingerprint_strings"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
