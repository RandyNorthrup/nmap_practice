#!/usr/bin/env python3
"""Version all-ports override.

Use case: Version all-ports override practice profile with bounded Nmap options and saved output.
Core flags: -sT -sV --allports --version-light --reason --open
Risk: medium. Scope: loopback.
Modify matching scan_version_allports_lab row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_version_allports_lab"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
