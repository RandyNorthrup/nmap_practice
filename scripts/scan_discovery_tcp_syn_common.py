#!/usr/bin/env python3
"""TCP SYN discovery.

Use case: TCP SYN discovery practice profile with bounded Nmap options and saved output.
Core flags: -sn -PS22,80,443 --reason
Risk: low. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_discovery_tcp_syn_common row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discovery_tcp_syn_common"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
