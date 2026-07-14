#!/usr/bin/env python3
"""Full version detection.

Use case: Full version detection practice profile with bounded Nmap options and saved output.
Core flags: -sT -sV --version-all --reason --open
Risk: medium. Scope: authorized.
Modify matching scan_version_all_profile row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_version_all_profile"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
