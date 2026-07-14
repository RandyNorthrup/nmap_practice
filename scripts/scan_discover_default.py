#!/usr/bin/env python3
"""Default discovery.

Use case: Use Nmap default host discovery probes without port scan.
Core flags: -sn
Risk: low. Scope: private.
Modify matching scan_discover_default row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discover_default"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
