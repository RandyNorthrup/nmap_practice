#!/usr/bin/env python3
"""Known-up TCP.

Use case: Skip discovery and scan a known-up host.
Core flags: -sT -Pn --top-ports 100
Risk: medium. Scope: authorized.
Modify matching scan_tcp_no_ping row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_no_ping"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
