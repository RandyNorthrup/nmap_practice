#!/usr/bin/env python3
"""Test double that records Nmap arguments without sending network traffic."""

import json
import os
from pathlib import Path
import sys


log_path = os.environ.get("MOCK_NMAP_LOG")
if not log_path:
    print("MOCK_NMAP_LOG must be set", file=sys.stderr)
    raise SystemExit(2)
Path(log_path).write_text(json.dumps(sys.argv[1:]), encoding="utf-8")
