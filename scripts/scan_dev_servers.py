#!/usr/bin/env python3
"""Development servers.

Use case: Inventory development servers with TCP connect and light service detection.
Core flags: -sT -sV --version-light --reason --open
Risk: low. Scope: authorized.
Modify matching scan_dev_servers row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_dev_servers"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
