#!/usr/bin/env python3
"""UDP service detection.

Use case: UDP service detection practice profile with bounded Nmap options and saved output.
Core flags: -sU -sV --version-light --reason --open
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_udp_version_common row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_udp_version_common"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
