#!/usr/bin/env python3
"""VNC information.

Use case: VNC information: run the installed vnc-info NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script vnc-info --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_vnc_info row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_vnc_info"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
