#!/usr/bin/env python3
"""Loopback-only synthetic services for Nmap practice."""

from __future__ import annotations

import http.server
import argparse
import signal
import socketserver
import threading
from urllib.parse import urlsplit


HOST = "127.0.0.1"
HEALTH_TOKEN = ""


class ReusableThreadingTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


class ReusableThreadingUDPServer(socketserver.ThreadingUDPServer):
    allow_reuse_address = True
    daemon_threads = True


class HttpHandler(http.server.BaseHTTPRequestHandler):
    server_version = "NmapPracticeHTTP/1.0"

    def do_GET(self) -> None:  # noqa: N802 - standard library method name
        if urlsplit(self.path).path == "/health":
            # Token lets lab manager verify process identity before stopping it.
            body = f"{HEALTH_TOKEN}\n".encode("utf-8")
            status = 200
        else:
            body = (
                b"Nmap practice HTTP service\n"
                b"Try: nmap -sV -p 8000 127.0.0.1\n"
            )
            status = 200
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        return


class SshBannerHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        self.request.settimeout(2)
        self.request.sendall(b"SSH-2.0-NmapPractice_1.0\r\n")
        try:
            self.request.recv(1024)
        except TimeoutError:
            pass


class EchoHandler(socketserver.StreamRequestHandler):
    def handle(self) -> None:
        self.wfile.write(b"NMAP-PRACTICE ECHO 1.0\n")
        self.wfile.flush()
        self.connection.settimeout(2)
        try:
            line = self.rfile.readline(1024)
        except TimeoutError:
            return
        if line:
            self.wfile.write(b"ECHO: " + line)


class UdpHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        _data, sock = self.request
        sock.sendto(b"NMAP-PRACTICE UDP 1.0\n", self.client_address)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Loopback-only Nmap practice services")
    parser.add_argument("--token", required=True, help=argparse.SUPPRESS)
    return parser


def main() -> None:
    global HEALTH_TOKEN
    HEALTH_TOKEN = build_parser().parse_args().token
    servers: list[socketserver.BaseServer] = []
    threads: list[threading.Thread] = []
    stopped = threading.Event()

    def request_stop(_signum: int, _frame: object) -> None:
        stopped.set()

    signal.signal(signal.SIGTERM, request_stop)
    signal.signal(signal.SIGINT, request_stop)

    configurations = (
        (ReusableThreadingTCPServer, 2222, SshBannerHandler),
        (ReusableThreadingTCPServer, 8000, HttpHandler),
        (ReusableThreadingTCPServer, 9000, EchoHandler),
        (ReusableThreadingUDPServer, 5353, UdpHandler),
    )

    try:
        for server_class, port, handler in configurations:
            server = server_class((HOST, port), handler)
            servers.append(server)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            threads.append(thread)

        print("READY tcp=2222,8000,9000 udp=5353 host=127.0.0.1", flush=True)
        stopped.wait()
    finally:
        for server in servers:
            server.shutdown()
            server.server_close()
        for thread in threads:
            thread.join(timeout=2)


if __name__ == "__main__":
    main()
