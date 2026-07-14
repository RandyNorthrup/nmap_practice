#!/usr/bin/env python3
"""SCTP discovery.

Use case: Discover SCTP hosts with INIT probes.
Core flags: -sn -PY80,2905
Risk: low. Scope: private. Raw packets may need elevated privileges.
Modify matching scan_discover_sctp row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discover_sctp"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
