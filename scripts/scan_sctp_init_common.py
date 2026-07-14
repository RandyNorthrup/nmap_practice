#!/usr/bin/env python3
"""SCTP INIT scan.

Use case: SCTP INIT scan practice profile with bounded Nmap options and saved output.
Core flags: -sY --reason --open
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_sctp_init_common row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_sctp_init_common"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
