#!/usr/bin/env python3
"""Common-port SYN discovery.

Use case: Discover hosts using SYN probes to SSH and web ports.
Core flags: -sn -PS22,80,443
Risk: low. Scope: private. Raw packets may need elevated privileges.
Modify matching scan_discover_syn_common row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discover_syn_common"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
