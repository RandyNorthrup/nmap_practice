#!/usr/bin/env python3
"""EtherNet/IP information.

Use case: EtherNet/IP information: run the installed enip-info NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script enip-info --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_enip_info row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_enip_info"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
