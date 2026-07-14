#!/usr/bin/env python3
"""Infrastructure: X11 unauthenticated access.

Use case: Run bounded x11-access NSE checks for X11 unauthenticated access on authorized services.
Core flags: -sT -sV --version-light --script x11-access --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_x11_access row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_x11_access"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
