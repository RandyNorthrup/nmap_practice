#!/usr/bin/env python3
"""MQTT subscription sample.

Use case: MQTT subscription sample: run the installed mqtt-subscribe NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script mqtt-subscribe --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_mqtt_subscribe_private row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_mqtt_subscribe_private"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
