# Progressive practice labs

Examples use `python3`; Windows PowerShell users replace it with `py`. Complete
loopback track first. Private-network track requires devices and network you own
or have explicit permission to scan.

For every lab, record:

1. Prediction.
2. Exact command.
3. Relevant output.
4. Why Nmap reached that result.
5. One safe follow-up question.

## Track overview

| Track | Labs | Target |
|---|---|---|
| Setup and navigation | 0–2 | No traffic or loopback |
| TCP, service, HTTP, NSE, UDP | 3–8 | Loopback lab |
| Results and automation | 9–12 | Loopback lab/XML |
| Authorized private network | 13–18 | Owned private hosts |
| Extension work | 19 | Loopback and code |

## Lab 0: verify installation and tests

```bash
nmap --version
python3 tests/run_tests.py
```

Expected: Nmap version and passing suite. Tests use mock Nmap for command building
plus real loopback TCP/UDP lab lifecycle.

## Lab 1: navigate 358 profiles

No scan traffic:

```bash
python3 scripts/profile_catalog.py --category discovery
python3 scripts/profile_catalog.py --search http
python3 scripts/profile_catalog.py --scope loopback
python3 scripts/profile_catalog.py --category tls --risk low --json
```

Questions:

1. How many discovery profiles exist?
2. Which HTTP profiles are loopback-only?
3. Which TLS profiles may need elevated privileges?
4. How does runtime catalog differ from static catalog?

Static reference: [complete profile catalog](profile-catalog.md).

## Lab 2: dry-run and scope guards

```bash
python3 scripts/scan_tcp_top_100.py 127.0.0.1 --dry-run
python3 scripts/scan_http_drupal_loopback.py 127.0.0.1 --dry-run
python3 scripts/scan_http_drupal_loopback.py 192.168.1.10 --dry-run
```

First two commands print Nmap commands without traffic. Third must fail because
high-risk Drupal enumeration profile is loopback-only.

Try shared options:

```bash
python3 scripts/scan_http_headers.py 127.0.0.1 \
  --ports 8000 --no-dns -vv --output results/dry-http --dry-run
```

## Lab 3: open and closed TCP states

```bash
python3 scripts/lab.py start
python3 scripts/lab.py status
python3 scripts/scan_tcp_connect.py 127.0.0.1 \
  --ports 2221-2223,8000,9000,9001 --output results/lab-states
```

Questions:

1. Which ports are open?
2. Why do 2221, 2223, and 9001 show closed?
3. What does `conn-refused` mean?
4. Why can port-based service name differ from real service?

## Lab 4: service-detection intensity

Run three bounded profiles:

```bash
python3 scripts/scan_version_intensity_zero.py 127.0.0.1 \
  --ports 2222,8000,9000 --output results/version-0
python3 scripts/scan_version_intensity_default.py 127.0.0.1 \
  --ports 2222,8000,9000 --output results/version-5
python3 scripts/scan_version_intensity_nine.py 127.0.0.1 \
  --ports 2222,8000,9000 --output results/version-9
```

Compare duration, number of probes, service confidence, and fingerprints. More
probes do not guarantee correct identification.

## Lab 5: HTTP profiles

```bash
python3 scripts/scan_http_title.py 127.0.0.1 --ports 8000
python3 scripts/scan_http_headers.py 127.0.0.1 --ports 8000
python3 scripts/scan_http_security_headers.py 127.0.0.1 --ports 8000
python3 scripts/scan_http_methods.py 127.0.0.1 --ports 8000
```

Expected: lab serves plain text without HTML title. Missing title is valid result.
Compare server header, content type, security-header findings, and allowed methods.

## Lab 6: focused NSE and script arguments

Inspect installed NSE help:

```bash
nmap --script-help http-title
nmap --script-help ssh-auth-methods
```

Preview SSH arguments:

```bash
python3 scripts/scan_ssh_auth_methods.py 127.0.0.1 \
  --ports 2222 --script-args "ssh.user=practice" --dry-run
```

Synthetic SSH service sends banner but does not complete handshake. Empty/partial
NSE result is expected. Explain difference between no finding and failed scan.

## Lab 7: UDP states

Linux/macOS elevated terminal:

```bash
sudo python3 scripts/scan_udp_common.py 127.0.0.1 --ports 5352-5354
```

Windows Administrator PowerShell:

```powershell
py scripts/scan_udp_common.py 127.0.0.1 --ports 5352-5354
```

Port 5353 responds; neighbors do not. Explain why UDP silence can produce
`open|filtered` instead of `closed`.

## Lab 8: packet trace and scan mechanics

Loopback-only profile:

```bash
python3 scripts/scan_tcp_packet_trace_lab.py 127.0.0.1 --ports 8000
```

Then compare connect and elevated SYN scans:

```bash
python3 scripts/scan_tcp_connect.py 127.0.0.1 --ports 2222,8000,9000
python3 scripts/scan_tcp_syn.py 127.0.0.1 --ports 2222,8000,9000
```

SYN may need elevation. Identify SYN, SYN/ACK, RST, and completed TCP connection.

## Lab 9: validate and convert XML

Use saved `results/lab-states.xml`:

```bash
python3 scripts/report_validate.py results/lab-states.xml
python3 scripts/report_summary.py results/lab-states.xml
python3 scripts/report_json.py results/lab-states.xml --output results/lab-states.json
python3 scripts/report_csv.py results/lab-states.xml --output results/lab-states.csv
python3 scripts/report_markdown.py results/lab-states.xml --output results/lab-states.md
python3 scripts/report_open_ports.py results/lab-states.xml
```

Compare what `.nmap`, XML, JSON, CSV, and Markdown preserve.

## Lab 10: compare service changes

Create running baseline, stop lab, create stopped baseline:

```bash
python3 scripts/scan_tcp_connect.py 127.0.0.1 \
  --ports 2222,8000,9000 --output results/lab-running
python3 scripts/lab.py stop
python3 scripts/scan_tcp_connect.py 127.0.0.1 \
  --ports 2222,8000,9000 --output results/lab-stopped
python3 scripts/compare_results.py results/lab-running.xml results/lab-stopped.xml
```

Expected: same ports change from open to closed.

## Lab 11: focused rescan from XML

Restart lab and preview rescan:

```bash
python3 scripts/lab.py start
python3 scripts/rescan_open_ports.py results/lab-running.xml --dry-run
python3 scripts/rescan_open_ports.py results/lab-running.xml
```

Observe extracted targets/ports and difference between TCP service and UDP rescan.

## Lab 12: bounded watch

```bash
python3 scripts/watch_profile.py scan_tcp_connect 127.0.0.1 \
  --count 2 --interval 10 --output-dir results/watch-practice
```

No changes expected while lab stays stable. Repeat manually with lab stopped
between scans if you want a state change; do not bypass finite-count guard.

## Lab 13: identify owned private network

Find local address and route:

- Linux: `ip -brief address` and `ip route`
- macOS: `ifconfig` and `route -n get default`
- Windows PowerShell: `Get-NetIPAddress` and `Get-NetRoute`

Write exact owned CIDR. Do not copy example blindly. Preview:

```bash
python3 scripts/scan_discovery_arp.py 192.168.1.0/24 --dry-run
```

## Lab 14: compare discovery methods

Against owned private subnet:

```bash
python3 scripts/scan_discovery_arp.py 192.168.1.0/24
python3 scripts/scan_discovery_icmp_echo.py 192.168.1.0/24
python3 scripts/scan_discovery_tcp_syn_common.py 192.168.1.0/24
python3 scripts/scan_discovery_udp_common.py 192.168.1.0/24
```

Why might result sets differ? Consider local ARP visibility, firewall rules,
sleeping devices, and raw-packet privilege.

## Lab 15: inventory one owned host

Choose one discovered device:

```bash
python3 scripts/scan_tcp_top_100.py 192.168.1.10
python3 scripts/scan_service_light.py 192.168.1.10
python3 scripts/scan_linux_service_ports.py 192.168.1.10
```

If device is Windows, use `scan_windows_service_ports.py`. If unknown, avoid
assuming operating system from port names alone.

## Lab 16: protocol tracks

Choose only protocols expected on owned host:

```bash
python3 scripts/scan_tls_certificate.py 192.168.1.10 --ports 443
python3 scripts/scan_ssh_algorithms.py 192.168.1.10 --ports 22
python3 scripts/scan_smb_protocols.py 192.168.1.10 --ports 445
python3 scripts/scan_dns_nsid.py 192.168.1.10 --ports 53
python3 scripts/scan_mysql_info.py 192.168.1.10 --ports 3306
```

Do not run every protocol profile blindly. Match profile to known or discovered
service.

## Lab 17: firewall-state comparison

From elevated terminal against one owned private host:

```bash
python3 scripts/scan_tcp_syn.py 192.168.1.10 --ports 22,80,443
python3 scripts/scan_tcp_ack.py 192.168.1.10 --ports 22,80,443
python3 scripts/scan_tcp_window.py 192.168.1.10 --ports 22,80,443
```

Compare `open`, `closed`, `filtered`, and `unfiltered`. ACK/Window do not answer
same question as SYN.

## Lab 18: batch inventory

Create reviewed target file with two or three owned hosts:

```text
192.168.1.10
192.168.1.20
```

```bash
python3 scripts/batch_profile.py scan_tcp_top_100 targets.txt --dry-run
python3 scripts/batch_profile.py scan_tcp_top_100 targets.txt \
  --output-dir results/private-batch
```

Inspect numbered outputs and summarize:

```bash
python3 scripts/report_stats.py "results/private-batch/*.xml"
```

## Lab 19: add a profile

Follow [script architecture guide](script-guide.md):

1. Add low-risk loopback row to `profile_extras.py`.
2. Add matching entry script and docstring.
3. Regenerate `profile-catalog.md`.
4. Run full tests.
5. Dry-run new profile.
6. Smoke-test only against loopback.

Stop lab when done:

```bash
python3 scripts/lab.py stop
```
