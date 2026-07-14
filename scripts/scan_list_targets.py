#!/usr/bin/env python3
"""List targets.

Use case: List target addresses without discovery or port probes.
Core flags: -sL
Risk: low. Scope: private.
Modify matching scan_list_targets row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_list_targets"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
