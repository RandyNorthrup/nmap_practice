#!/usr/bin/env python3
"""TCP SYN top 100.

Use case: TCP SYN top 100 practice profile with bounded Nmap options and saved output.
Core flags: -sS --top-ports 100 --reason --open
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_tcp_syn_top100 row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_syn_top100"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
