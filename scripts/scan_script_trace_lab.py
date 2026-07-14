#!/usr/bin/env python3
"""NSE loopback trace.

Use case: Trace conservative NSE traffic against local lab.
Core flags: -sT -sV --script default and safe --script-trace
Risk: high. Scope: loopback.
Modify matching scan_script_trace_lab row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_script_trace_lab"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
