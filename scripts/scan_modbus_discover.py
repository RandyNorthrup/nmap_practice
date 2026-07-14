#!/usr/bin/env python3
"""Infrastructure: Modbus identification.

Use case: Run bounded modbus-discover NSE checks for Modbus identification on authorized services.
Core flags: -sT -sV --version-light --script modbus-discover --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_modbus_discover row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_modbus_discover"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
