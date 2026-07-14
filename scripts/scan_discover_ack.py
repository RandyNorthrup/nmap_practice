#!/usr/bin/env python3
"""ACK discovery.

Use case: Discover hosts with TCP ACK probes.
Core flags: -sn -PA22,80,443
Risk: low. Scope: private. Raw packets may need elevated privileges.
Modify matching scan_discover_ack row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discover_ack"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
