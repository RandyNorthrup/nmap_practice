#!/usr/bin/env python3
"""TCP packet trace.

Use case: Print packets for a tiny loopback scan.
Core flags: -sT --packet-trace
Risk: high. Scope: loopback.
Modify matching scan_tcp_packet_trace row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_packet_trace"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
