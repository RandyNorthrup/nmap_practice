#!/usr/bin/env python3
"""Infrastructure: RTSP methods.

Use case: Run bounded rtsp-methods NSE checks for RTSP methods on authorized services.
Core flags: -sT -sV --version-light --script rtsp-methods --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_rtsp_methods row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_rtsp_methods"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
