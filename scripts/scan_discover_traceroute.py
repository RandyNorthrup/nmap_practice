#!/usr/bin/env python3
"""Discovery traceroute.

Use case: Discover a host and trace path without scanning ports.
Core flags: -sn --traceroute
Risk: low. Scope: authorized.
Modify matching scan_discover_traceroute row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discover_traceroute"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
