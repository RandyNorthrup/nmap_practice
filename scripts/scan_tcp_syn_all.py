#!/usr/bin/env python3
"""Full TCP SYN scan.

Use case: Full TCP SYN scan practice profile with bounded Nmap options and saved output.
Core flags: -sS -p- --reason --open
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_tcp_syn_all row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_syn_all"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
