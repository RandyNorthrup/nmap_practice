from __future__ import annotations

import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import unittest
from urllib.request import urlopen


ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "scripts" / "lab.py"


class LabLifecycleTests(unittest.TestCase):
    def test_start_health_udp_and_stop(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            environment = os.environ.copy()
            environment["NMAP_PRACTICE_RUNTIME_DIR"] = directory

            start = subprocess.run(
                [sys.executable, str(LAB), "start"],
                capture_output=True,
                text=True,
                env=environment,
                check=False,
            )
            self.assertEqual(0, start.returncode, start.stderr)
            try:
                state = json.loads((Path(directory) / "lab.json").read_text(encoding="utf-8"))
                with urlopen("http://127.0.0.1:8000/health", timeout=2) as response:  # noqa: S310
                    self.assertEqual(state["token"], response.read().decode().strip())

                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp:
                    udp.settimeout(2)
                    udp.sendto(b"hello", ("127.0.0.1", 5353))
                    data, _address = udp.recvfrom(1024)
                    self.assertIn(b"NMAP-PRACTICE UDP", data)
            finally:
                stop = subprocess.run(
                    [sys.executable, str(LAB), "stop"],
                    capture_output=True,
                    text=True,
                    env=environment,
                    check=False,
                )
            self.assertEqual(0, stop.returncode, stop.stderr)


if __name__ == "__main__":
    unittest.main()
