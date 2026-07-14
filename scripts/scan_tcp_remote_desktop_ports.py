#!/usr/bin/env python3
"""Remote-display ports.

Use case: Scan RDP, VNC, and X11 ports.
Core flags: -sT
Risk: low. Scope: authorized.
Modify matching scan_tcp_remote_desktop_ports row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_remote_desktop_ports"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
