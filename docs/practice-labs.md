# Progressive practice labs

Complete labs in order. Examples use `python3`; use `py` in Windows PowerShell.
Keep notes with command, prediction, result, and explanation.

## Lab 0: verify setup

```bash
nmap --version
python3 tests/run_tests.py
```

Look for Nmap version output and passing tests. No Nmap scan happens here.

## Lab 1: open and closed TCP ports

```bash
python3 scripts/lab.py start
python3 scripts/lab.py status
python3 scripts/scan_ports.py 127.0.0.1 --ports 2221-2223,8000,9000,9001 --show-closed
```

Questions:

1. Which ports are open?
2. Why do 2221, 2223, and 9001 differ from listening ports?
3. What reason does Nmap provide for each state?

Repeat using raw Nmap with more detail:

```bash
nmap -sT -p 2221-2223,8000,9000,9001 --reason -vv 127.0.0.1
```

## Lab 2: service detection

```bash
python3 scripts/scan_services.py 127.0.0.1 --ports 2222,8000,9000
```

Compare `SERVICE` and `VERSION` with README lab table. Nmap guesses from port
numbers, banners, and probe responses. A guess is not proof.

```bash
python3 scripts/scan_services.py 127.0.0.1 --ports 2222,8000,9000 --version-all
```

Questions:

1. Which banner causes SSH-like identification?
2. Does port 9000 receive a confident service name?
3. How do light and full version probing differ in time and output?

## Lab 3: web inspection

```bash
python3 scripts/scan_web.py 127.0.0.1 --ports 8000
```

Find HTTP status, server header, content type, and page title result. Lab page has
no HTML title, so `http-title` may show no title; modify `lab/server.py` to return
HTML, update its test, then retry.

## Lab 4: safe NSE scripts

```bash
python3 scripts/scan_safe_scripts.py 127.0.0.1 --ports 2222,8000
nmap --script-help "default and safe"
```

Synthetic SSH service does not complete a real handshake. Some scripts produce
no output or stop early; this is expected.

## Lab 5: UDP ambiguity

Linux/macOS elevated terminal:

```bash
sudo python3 scripts/scan_udp.py 127.0.0.1 --ports 5352-5354
```

Windows: open PowerShell as Administrator, then run:

```powershell
py scripts/scan_udp.py 127.0.0.1 --ports 5352-5354
```

UDP has no connection handshake. Response can establish `open`; silence can mean
ignored probe, firewall, packet loss, or no listener. Compare 5353 with neighbors.

## Lab 6: save and compare changes

Run each command on one line so examples work in Bash and PowerShell:

```bash
python3 scripts/scan_ports.py 127.0.0.1 --ports 2222,8000,9000 --output results/lab-running
python3 scripts/lab.py stop
python3 scripts/scan_ports.py 127.0.0.1 --ports 2222,8000,9000 --show-closed --output results/lab-stopped
python3 scripts/compare_results.py results/lab-running.xml results/lab-stopped.xml
```

Comparator reports added, removed, and changed ports. XML is for tools; `.nmap`
is easiest for people; `.gnmap` is legacy line-oriented output.

## Lab 7: discover your own LAN

Find your local address and route:

- Linux: `ip -brief address` and `ip route`
- macOS: `ifconfig` and `route -n get default`
- Windows PowerShell: `Get-NetIPAddress` and `Get-NetRoute`

If an owned LAN is `192.168.1.0/24`:

```bash
python3 scripts/scan_discovery.py 192.168.1.0/24
```

Do not copy example subnet blindly. Discovery can miss sleeping or filtered hosts.
Choose one device you own, predict likely services, then scan narrowly:

```bash
python3 scripts/scan_ports.py 192.168.1.10 --ports 22,53,80,443 --show-closed
```

## Lab 8: connect versus SYN scans

```bash
python3 scripts/lab.py start
python3 scripts/scan_ports.py 127.0.0.1 --ports 2222,8000,9000 --output results/connect
```

Run SYN scan in elevated terminal:

```bash
python3 scripts/scan_ports.py 127.0.0.1 --syn --ports 2222,8000,9000 --output results/syn
```

Connect scans ask operating system to complete TCP connections. SYN scans use raw
packets. Compare printed scan type, result, and packet behavior.

## Lab 9: route and OS guesses

Use `scan_route.py` against an authorized private host beyond loopback:

```bash
python3 scripts/scan_route.py 192.168.1.10
```

Then, from elevated terminal:

```bash
python3 scripts/scan_os.py 192.168.1.10
```

Router filtering can hide hops. OS fingerprints are probabilistic and work best
when Nmap sees at least one open and one closed TCP port.

Stop lab:

```bash
python3 scripts/lab.py stop
```

## Next experiments

- Capture your own loopback traffic with Wireshark and map packets to port states.
- Add a loopback service to `lab/server.py`, update tests, then predict `-sV` output.
- Follow [script modification guide](script-guide.md) to add a custom use case.
