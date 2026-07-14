# Nmap and practice-suite cheat sheet

Examples use `python3`; Windows PowerShell users use `py`.

## Start here

| Goal | Suite command |
|---|---|
| Search profiles | `python3 scripts/profile_catalog.py --search tls` |
| List category | `python3 scripts/profile_catalog.py --category discovery` |
| Show high-risk loopback profiles | `python3 scripts/profile_catalog.py --risk high` |
| Inspect without traffic | `python3 scripts/scan_tcp_top_100.py 127.0.0.1 --dry-run` |
| Start/stop lab | `python3 scripts/lab.py start` / `python3 scripts/lab.py stop` |
| Run tests | `python3 tests/run_tests.py` |

## Common Nmap tasks and profiles

| Goal | Raw Nmap | Focused profile |
|---|---|---|
| Host discovery | `nmap -sn TARGET` | `scan_discover_default.py` |
| ARP discovery | `nmap -sn -PR CIDR` | `scan_discovery_arp.py` |
| Top 100 TCP | `nmap -sT --top-ports 100 TARGET` | `scan_tcp_top_100.py` |
| Selected TCP | `nmap -sT -p 22,80,443 TARGET` | `scan_tcp_connect.py --ports 22,80,443` |
| SYN scan | `nmap -sS -p 22,80,443 TARGET` | `scan_tcp_syn.py --ports 22,80,443` |
| Common UDP | `nmap -sU -p 53,123,161 TARGET` | `scan_udp_common.py --ports 53,123,161` |
| Service detection | `nmap -sT -sV TARGET` | `scan_service_default.py` |
| OS fingerprint | `nmap -O TARGET` | `scan_os_fingerprint.py` |
| TLS certificate | `nmap --script ssl-cert -p 443 TARGET` | `scan_tls_certificate.py --ports 443` |
| HTTP headers | `nmap --script http-headers -p 80 TARGET` | `scan_http_headers.py --ports 80` |
| Save all formats | `nmap -oA PREFIX TARGET` | Every suite scanner does this |

Replace `TARGET` only with authorized target. Raw-packet commands may need
elevation.

## Shared profile options

| Option | Meaning |
|---|---|
| `TARGET` | Authorized IP, CIDR, or hostname |
| `--output PREFIX` | Choose `.nmap`/`.gnmap`/`.xml` output prefix |
| `--allow-public` | Explicit non-private opt-in; not permission |
| `--ports LIST` | Override profile default ports when supported |
| `--timing T0..T4` | Override timing template |
| `--no-dns` | Disable reverse DNS (`-n`) |
| `--skip-host-discovery` | Treat target as online (`-Pn`) |
| `--script-args TEXT` | NSE arguments; NSE profiles only |
| `--extra-arg OPTION` | Add one advanced option; repeat for value |
| `-v`, `-vv`, `-vvv` | More verbosity |
| `--dry-run` | Validate and print command without scan |

## Nmap scan options

| Option | Meaning |
|---|---|
| `-sL` | List targets without discovery/port scan |
| `-sn` | Host discovery only |
| `-sT` | TCP connect scan; unprivileged |
| `-sS` | TCP SYN scan; usually elevated |
| `-sA` | TCP ACK firewall-state scan |
| `-sU` | UDP scan; usually elevated |
| `-sY` / `-sZ` | SCTP INIT / COOKIE-ECHO scan |
| `-sO` | IP protocol scan |
| `-p 80,443` | Exact ports |
| `-p-` | All ports 1–65535 |
| `--top-ports 100` | Nmap frequency-ranked ports |
| `-sV` | Service/version probes |
| `--version-light` | Fewer service probes |
| `-O` | OS fingerprinting |
| `--script NAME` | Run NSE script/expression |
| `--reason` | Explain state decision |
| `--open` | Show open/possibly-open results only |
| `-Pn` | Skip host discovery |
| `-n` / `-R` | Disable / force reverse DNS |
| `-T3` | Normal timing; suite default |
| `-oA PREFIX` | Normal, grepable, and XML outputs |

## Port states

| State | Plain meaning |
|---|---|
| `open` | Application responded or accepted connection |
| `closed` | Host replied but no listener on port |
| `filtered` | Firewall or packet loss blocked clear answer |
| `open|filtered` | Common UDP ambiguity: silence has multiple causes |
| `unfiltered` | Reachable, but scan type cannot decide open/closed |
| `closed|filtered` | Scan type cannot separate closed from filtered |

Service names are guesses from ports and probes. Verify important results with
configuration owners.

## Output and reports

| Need | Command |
|---|---|
| Validate XML | `python3 scripts/report_validate.py FILE.xml` |
| Human summary | `python3 scripts/report_summary.py FILE.xml` |
| Open ports | `python3 scripts/report_open_ports.py FILE.xml` |
| JSON | `python3 scripts/report_json.py FILE.xml --output report.json` |
| CSV | `python3 scripts/report_csv.py FILE.xml --output report.csv` |
| Markdown | `python3 scripts/report_markdown.py FILE.xml --output report.md` |
| Compare | `python3 scripts/compare_results.py OLD.xml NEW.xml` |
| Focused rescan | `python3 scripts/rescan_open_ports.py FILE.xml --dry-run` |

## CIDR reminders

| CIDR | IPv4 addresses | Practice advice |
|---|---:|---|
| `/32` | 1 | Best starting scope |
| `/30` | 4 | Tiny network |
| `/24` | 256 | Typical LAN; discovery first |
| `/16` | 65,536 | Large; do not scan casually |
