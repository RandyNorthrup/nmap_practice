#!/usr/bin/env python3
"""TCP FIN scan.

Use case: TCP FIN scan practice profile with bounded Nmap options and saved output.
Core flags: -sF --top-ports 100 --reason
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_tcp_fin_common row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_fin_common"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
