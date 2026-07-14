#!/usr/bin/env python3
"""Verbose discovery.

Use case: Run discovery with extra progress and reasons.
Core flags: -sn -vv --reason
Risk: low. Scope: private.
Modify matching scan_discover_verbose row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discover_verbose"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
