#!/usr/bin/env python3
"""SCTP INIT.

Use case: Scan common SCTP ports using INIT packets.
Core flags: -sY
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_sctp_init row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_sctp_init"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
