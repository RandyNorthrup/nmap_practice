#!/usr/bin/env python3
"""Canon BJNP discovery.

Use case: Canon BJNP discovery: run the installed bjnp-discover NSE script on expected service ports, with timeout and saved output.
Core flags: -sU -sV --version-light --script bjnp-discover --script-timeout 30s --open
Risk: medium. Scope: private. Raw packets may need elevated privileges.
Modify matching scan_bjnp_printer row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_bjnp_printer"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
