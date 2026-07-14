#!/usr/bin/env python3
"""Combined host discovery.

Use case: Combined host discovery practice profile with bounded Nmap options and saved output.
Core flags: -sn -PE -PS22,80,443 -PA80,443 -PU53,123 --reason
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_discovery_combined row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discovery_combined"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
