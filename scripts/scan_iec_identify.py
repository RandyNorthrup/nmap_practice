#!/usr/bin/env python3
"""Infrastructure: IEC 104 identification.

Use case: Run bounded iec-identify NSE checks for IEC 104 identification on authorized services.
Core flags: -sT -sV --version-light --script iec-identify --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_iec_identify row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_iec_identify"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
