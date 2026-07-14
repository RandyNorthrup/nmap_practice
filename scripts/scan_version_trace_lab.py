#!/usr/bin/env python3
"""Version probe trace.

Use case: Version probe trace practice profile with bounded Nmap options and saved output.
Core flags: -sT -sV --version-trace --reason --open
Risk: high. Scope: loopback.
Modify matching scan_version_trace_lab row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_version_trace_lab"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
