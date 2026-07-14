# Nmap Practice Kit

Robust, hands-on Nmap practice suite with more than 350 focused scan profiles,
cross-platform workflow tools, an isolated local lab, XML reporting, batch runs,
bounded monitoring, and change comparison.

> Scan only systems you own or have explicit permission to test. Public targets
> require `--allow-public`; that flag is a reminder, not permission.

## Platforms

All scripts use Python 3's standard library and work on Linux, macOS, and Windows.
Nmap and Python 3 must be installed and available in `PATH`.

- Linux/macOS examples use `python3`.
- Windows PowerShell users replace `python3` with `py`.
- SYN, UDP, and OS scans may need `sudo` on Linux/macOS or an Administrator
  terminal with Npcap on Windows. Nmap prints the exact privilege error.

## Quick start

Linux/macOS:

```bash
python3 tests/run_tests.py
python3 scripts/lab.py start
python3 scripts/scan_ports.py 127.0.0.1 --ports 2222,8000,9000
python3 scripts/scan_services.py 127.0.0.1 --ports 2222,8000,9000
python3 scripts/lab.py stop
```

Windows PowerShell:

```powershell
py tests/run_tests.py
py scripts/lab.py start
py scripts/scan_ports.py 127.0.0.1 --ports 2222,8000,9000
py scripts/scan_services.py 127.0.0.1 --ports 2222,8000,9000
py scripts/lab.py stop
```

Lab binds only to `127.0.0.1` and provides synthetic services:

| Protocol | Port | Practice service |
|---|---:|---|
| TCP | 2222 | SSH-like banner (not real SSH) |
| TCP | 8000 | Small HTTP server with `/health` |
| TCP | 9000 | Line-based echo/banner service |
| UDP | 5353 | Small UDP responder |

Scan output goes to `results/` in normal, grepable, and XML formats.

## Script collection

Suite contains 350+ one-purpose profile scripts plus flexible scanners and
workflow utilities. Profiles cover:

- Target listing, ARP, ICMP, TCP, UDP, SCTP, IPv6, and combined discovery
- Connect, SYN, ACK, Window, FIN, NULL, Xmas, Maimon, mixed, and protocol scans
- Version intensity, OS fingerprinting, RPC, banners, safe/default NSE suites
- HTTP, TLS, SSH, FTP, mail, SMB, RDP, VNC, NFS, DNS, and SNMP
- Databases, queues, containers, Hadoop, industrial protocols, printers, and IoT
- Common Linux, Windows, development, monitoring, backup, VoIP, and admin ports

Find exact script through catalog:

```bash
python3 scripts/profile_catalog.py --search tls
python3 scripts/profile_catalog.py --category discovery
python3 scripts/scan_tls_certificate.py 127.0.0.1 --dry-run
```

Every profile accepts `--help`, `--dry-run`, `--output`, `--timing`, `--no-dns`,
and verbosity options. Examples:

```bash
python3 scripts/scan_ports.py --help
python3 scripts/scan_discover_arp.py 192.168.1.0/24 --dry-run
python3 scripts/scan_tcp_top_1000.py 192.168.1.10
python3 scripts/scan_http_headers.py 127.0.0.1 --ports 8000
python3 scripts/compare_results.py results/older.xml results/newer.xml
```

Workflow/report tools:

| Script | Purpose |
|---|---|
| `profile_catalog.py` | Search/filter every validated profile |
| `batch_profile.py` | Run one profile against authorized target file |
| `watch_profile.py` | Repeat bounded runs and report changes |
| `rescan_open_ports.py` | Build focused service rescan from XML |
| `compare_results.py` | Compare two Nmap XML reports |
| `report_summary.py` | Human-readable XML summary |
| `report_json.py` / `report_csv.py` | Export structured results |
| `report_markdown.py` | Produce Markdown report |
| `report_hosts.py` / `report_open_ports.py` | Extract target/port lists |
| `report_services.py` / `report_scripts.py` | Group services or NSE findings |
| `report_validate.py` | Validate Nmap XML |

## Documentation

- [Progressive labs](docs/practice-labs.md): guided exercises and questions
- [Complete profile catalog](docs/profile-catalog.md): every profile, flag, port, and risk
- [Robust workflows](docs/workflows.md): batch, watch, rescan, and reporting examples
- [Script guide](docs/script-guide.md): what every script does and how to modify it
- [Command cheat sheet](docs/cheatsheet.md): options and output meanings
- [Safety rules](docs/safety.md): scope, permissions, and low-impact practice

Use a small private subnet you control. Avoid `-T5`, full port ranges, brute-force
scripts, vulnerability scripts, and OS detection until you understand their
traffic and have permission.

## Tests

Cross-platform command:

```bash
python3 tests/run_tests.py
```

Tests compile every Python file, dry-build every registered profile, enforce
scope/risk locks, verify every entry script, test reporting/batch/watch/rescan,
compare XML, and start/verify/stop local TCP/UDP lab. `make test` is optional.
