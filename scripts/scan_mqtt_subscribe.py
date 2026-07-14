#!/usr/bin/env python3
"""Infrastructure: MQTT system topics.

Use case: Run bounded mqtt-subscribe NSE checks for MQTT system topics on authorized services.
Core flags: -sT -sV --version-light --script mqtt-subscribe --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_mqtt_subscribe row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_mqtt_subscribe"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
