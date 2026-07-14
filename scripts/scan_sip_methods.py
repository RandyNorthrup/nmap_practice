#!/usr/bin/env python3
"""Infrastructure: SIP methods.

Use case: Run bounded sip-methods NSE checks for SIP methods on authorized services.
Core flags: -sU -sV --version-light --script sip-methods --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_sip_methods row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_sip_methods"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
