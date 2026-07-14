#!/usr/bin/env python3
"""AJP headers.

Use case: AJP headers: run the installed ajp-headers NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script ajp-headers --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_ajp_headers row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ajp_headers"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
