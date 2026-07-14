#!/usr/bin/env python3
"""SCTP COOKIE.

Use case: Study SCTP COOKIE ECHO response behavior.
Core flags: -sZ
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_sctp_cookie row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_sctp_cookie"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
