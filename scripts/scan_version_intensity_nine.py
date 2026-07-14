#!/usr/bin/env python3
"""Version intensity 9.

Use case: Version intensity 9 practice profile with bounded Nmap options and saved output.
Core flags: -sT -sV --version-intensity 9 --reason --open
Risk: low. Scope: authorized.
Modify matching scan_version_intensity_nine row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_version_intensity_nine"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
