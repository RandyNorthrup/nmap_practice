#!/usr/bin/env python3
"""OS fingerprint.

Use case: Attempt bounded OS fingerprinting.
Core flags: -O --osscan-limit --max-os-tries 1 --top-ports 1000
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_os_fingerprint row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_os_fingerprint"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
