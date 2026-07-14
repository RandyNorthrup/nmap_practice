#!/usr/bin/env python3
"""AJP methods.

Use case: AJP methods: run the installed ajp-methods NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script ajp-methods --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_ajp_methods row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ajp_methods"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
