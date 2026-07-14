#!/usr/bin/env python3
"""TCP packet trace.

Use case: TCP packet trace practice profile with bounded Nmap options and saved output.
Core flags: -sT --packet-trace --reason
Risk: high. Scope: loopback.
Modify matching scan_tcp_packet_trace_lab row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_packet_trace_lab"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
