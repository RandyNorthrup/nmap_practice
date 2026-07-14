#!/usr/bin/env python3
"""TCP window.

Use case: Study TCP window response behavior.
Core flags: -sW
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_tcp_window row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_window"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
