#!/usr/bin/env python3
"""Web-port SYN discovery.

Use case: Web-port SYN discovery practice profile with bounded Nmap options and saved output.
Core flags: -sn -PS80,443,8000,8080,8443 --reason
Risk: low. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_discovery_tcp_syn_web row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discovery_tcp_syn_web"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
