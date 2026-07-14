#!/usr/bin/env python3
"""Combined ICMP discovery.

Use case: Combine echo, timestamp, and address-mask probes.
Core flags: -sn -PE -PP -PM
Risk: low. Scope: private. Raw packets may need elevated privileges.
Modify matching scan_discover_icmp_combo row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discover_icmp_combo"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
