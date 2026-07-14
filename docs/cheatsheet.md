# Nmap cheat sheet

## Core commands

| Goal | Command | Main result |
|---|---|---|
| Check installation | `nmap --version` | Version and compiled features |
| Discover hosts | `nmap -sn 192.168.1.0/24` | Hosts Nmap considers up |
| Common TCP ports | `nmap -sT --top-ports 100 HOST` | Open, closed, or filtered TCP ports |
| Chosen TCP ports | `nmap -sT -p 22,80,443 HOST` | State of listed ports |
| All TCP ports | `nmap -sT -p- HOST` | Ports 1 through 65535; potentially slow |
| Detect services | `nmap -sT -sV --version-light HOST` | Service guesses and banner details |
| Explain states | `nmap -sT --reason HOST` | Packet-level reason for each state |
| Safe/default NSE | `nmap -sT -sV --script "default and safe" HOST` | Low-risk script findings |
| UDP ports | `nmap -sU -p 53,123,161 HOST` (elevated terminal) | UDP port states; often slow/ambiguous |
| Save all formats | `nmap -oA results/name HOST` | `.nmap`, `.gnmap`, and `.xml` files |

Replace `HOST` only with an authorized target.

## Useful options

| Option | Meaning |
|---|---|
| `-sn` | Host discovery only; no port scan |
| `-sT` | TCP connect scan; works without root |
| `-sS` | TCP SYN scan; normally needs elevated privileges |
| `-sU` | UDP scan; normally needs elevated privileges |
| `-p 80,443` | Scan exact ports |
| `-p-` | Scan all TCP ports |
| `--top-ports 100` | Scan Nmap's 100 most common ports |
| `-sV` | Probe open ports to identify services |
| `-O` | OS fingerprinting; root and permission recommended |
| `--reason` | Explain why Nmap assigned each state |
| `--open` | Display only hosts with open or possibly open ports |
| `-Pn` | Skip host discovery and treat target as online |
| `-T3` | Normal timing; kit default |
| `-v` / `-vv` | More progress and detail |
| `-oA PREFIX` | Save normal, grepable, and XML reports |

## Port states

| State | Plain meaning |
|---|---|
| `open` | Application accepted or responded to Nmap's probe |
| `closed` | Host replied, but no application listens on that port |
| `filtered` | Firewall or packet loss prevented a clear answer |
| `open|filtered` | Common with UDP: no reply cannot distinguish open from blocked |
| `unfiltered` | Port is reachable, but scan type cannot tell open from closed |

Service names are educated guesses based on ports and probes. Verify important
findings with application owners and configuration data.

## CIDR reminders

| CIDR | Addresses | Typical use |
|---|---:|---|
| `/32` | 1 | One IPv4 host |
| `/30` | 4 | Very small network |
| `/24` | 256 | Common home LAN subnet |
| `/16` | 65,536 | Large; do not scan casually |
