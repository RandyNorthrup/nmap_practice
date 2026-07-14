#!/usr/bin/env python3
"""CoAP resources.

Use case: CoAP resources: run the installed coap-resources NSE script on expected service ports, with timeout and saved output.
Core flags: -sU -sV --version-light --script coap-resources --script-timeout 30s --open
Risk: medium. Scope: private. Raw packets may need elevated privileges.
Modify matching scan_coap_resources row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_coap_resources"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
