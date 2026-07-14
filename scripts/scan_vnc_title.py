#!/usr/bin/env python3
"""Infrastructure: VNC desktop title.

Use case: Run bounded vnc-title NSE checks for VNC desktop title on authorized services.
Core flags: -sT -sV --version-light --script vnc-title --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_vnc_title row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_vnc_title"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
