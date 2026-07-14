#!/usr/bin/env python3
"""Light version detection.

Use case: Light version detection practice profile with bounded Nmap options and saved output.
Core flags: -sT -sV --version-light --reason --open
Risk: low. Scope: authorized.
Modify matching scan_version_light_profile row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_version_light_profile"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
