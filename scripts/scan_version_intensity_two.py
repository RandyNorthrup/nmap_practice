#!/usr/bin/env python3
"""Version intensity 2.

Use case: Version intensity 2 practice profile with bounded Nmap options and saved output.
Core flags: -sT -sV --version-intensity 2 --reason --open
Risk: low. Scope: authorized.
Modify matching scan_version_intensity_two row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_version_intensity_two"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
