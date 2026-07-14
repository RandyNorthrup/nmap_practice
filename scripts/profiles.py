"""Registry powering more than 100 focused Nmap practice scripts.

Each profile records exact Nmap arguments, default ports, scope, risk, and
privilege expectations. Brute-force, denial-of-service, exploit, credential
dumping, spoofing, and public-target evasion profiles remain excluded.
"""

from __future__ import annotations

from dataclasses import dataclass

from profile_extras import EXTRA_PROFILE_DATA


@dataclass(frozen=True, slots=True)
class ScanProfile:
    name: str
    category: str
    title: str
    description: str
    arguments: tuple[str, ...]
    default_ports: str | None = None
    scope: str = "authorized"
    risk: str = "low"
    elevated: bool = False
    timing: str | None = "T3"


def profile(
    name: str,
    category: str,
    title: str,
    description: str,
    arguments: tuple[str, ...],
    default_ports: str | None = None,
    scope: str = "authorized",
    risk: str = "low",
    elevated: bool = False,
    timing: str | None = "T3",
) -> ScanProfile:
    return ScanProfile(
        name, category, title, description, arguments, default_ports,
        scope, risk, elevated, timing
    )


# Core rows use explicit flags because each teaches a different Nmap scan mode.
CORE_ROWS: tuple[ScanProfile, ...] = (
    profile("scan_list_targets", "discovery", "List targets", "List target addresses without discovery or port probes.", ("-sL",), scope="private", timing=None),
    profile("scan_list_targets_dns", "discovery", "List targets with DNS", "List targets and force reverse DNS without port scanning.", ("-sL", "-R"), scope="private", timing=None),
    profile("scan_discover_default", "discovery", "Default discovery", "Use Nmap default host discovery probes without port scan.", ("-sn",), scope="private"),
    profile("scan_discover_no_dns", "discovery", "Discovery without DNS", "Discover hosts without reverse DNS delays.", ("-sn", "-n"), scope="private"),
    profile("scan_discover_arp", "discovery", "ARP discovery", "Use ARP discovery on local Ethernet.", ("-sn", "-PR"), scope="private", elevated=True),
    profile("scan_discover_icmp_echo", "discovery", "ICMP echo discovery", "Use ICMP echo requests for discovery.", ("-sn", "-PE"), scope="private", elevated=True),
    profile("scan_discover_icmp_timestamp", "discovery", "ICMP timestamp discovery", "Use ICMP timestamp requests for discovery.", ("-sn", "-PP"), scope="private", elevated=True),
    profile("scan_discover_icmp_mask", "discovery", "ICMP mask discovery", "Use ICMP address-mask requests for discovery.", ("-sn", "-PM"), scope="private", elevated=True),
    profile("scan_discover_icmp_combo", "discovery", "Combined ICMP discovery", "Combine echo, timestamp, and address-mask probes.", ("-sn", "-PE", "-PP", "-PM"), scope="private", elevated=True),
    profile("scan_discover_syn_common", "discovery", "Common-port SYN discovery", "Discover hosts using SYN probes to SSH and web ports.", ("-sn", "-PS22,80,443"), scope="private", elevated=True),
    profile("scan_discover_syn_web", "discovery", "Web-port SYN discovery", "Discover web hosts with several HTTP and HTTPS ports.", ("-sn", "-PS80,443,8000,8080,8443"), scope="private", elevated=True),
    profile("scan_discover_ack", "discovery", "ACK discovery", "Discover hosts with TCP ACK probes.", ("-sn", "-PA22,80,443"), scope="private", elevated=True),
    profile("scan_discover_udp", "discovery", "UDP discovery", "Discover hosts with narrow DNS, NTP, and SNMP probes.", ("-sn", "-PU53,123,161"), scope="private", elevated=True),
    profile("scan_discover_sctp", "discovery", "SCTP discovery", "Discover SCTP hosts with INIT probes.", ("-sn", "-PY80,2905"), scope="private", elevated=True),
    profile("scan_discover_ip_protocol", "discovery", "IP protocol discovery", "Discover hosts using selected IP protocols.", ("-sn", "-PO1,2,4"), scope="private", elevated=True),
    profile("scan_discover_traceroute", "discovery", "Discovery traceroute", "Discover a host and trace path without scanning ports.", ("-sn", "--traceroute")),
    profile("scan_discover_ipv6", "discovery", "IPv6 discovery", "Run default host discovery over IPv6.", ("-6", "-sn")),
    profile("scan_discover_verbose", "discovery", "Verbose discovery", "Run discovery with extra progress and reasons.", ("-sn", "-vv", "--reason"), scope="private"),

    profile("scan_tcp_top_10", "transport", "Top 10 TCP", "TCP connect scan of ten common ports.", ("-sT", "--top-ports", "10")),
    profile("scan_tcp_top_100", "transport", "Top 100 TCP", "TCP connect scan of 100 common ports.", ("-sT", "--top-ports", "100")),
    profile("scan_tcp_top_1000", "transport", "Top 1000 TCP", "TCP connect scan of 1000 common ports.", ("-sT", "--top-ports", "1000"), risk="medium"),
    profile("scan_tcp_fast", "transport", "Fast TCP", "Use Nmap fast-mode port set.", ("-sT", "-F")),
    profile("scan_tcp_full", "transport", "Full TCP", "Scan all 65535 TCP ports on one authorized host.", ("-sT", "-p-"), risk="medium"),
    profile("scan_tcp_common", "transport", "Common services", "Scan common infrastructure TCP ports.", ("-sT",), "21,22,23,25,53,80,110,139,143,443,445,587,993,995,3389"),
    profile("scan_tcp_web_ports", "transport", "Web ports", "Scan common web and development server ports.", ("-sT",), "80,443,3000,5000,8000,8008,8080,8081,8443,8888"),
    profile("scan_tcp_admin_ports", "transport", "Administration ports", "Scan common remote administration ports.", ("-sT",), "22,23,161,443,445,3389,5900,5985,5986"),
    profile("scan_tcp_file_ports", "transport", "File-service ports", "Scan common file transfer and sharing ports.", ("-sT",), "20,21,22,111,139,445,873,2049"),
    profile("scan_tcp_mail_ports", "transport", "Mail ports", "Scan SMTP, POP3, and IMAP ports.", ("-sT",), "25,110,143,465,587,993,995"),
    profile("scan_tcp_database_ports", "transport", "Database ports", "Scan common database and cache ports.", ("-sT",), "523,1433,1521,27017,3306,5432,5984,6379,9042,11211"),
    profile("scan_tcp_remote_desktop_ports", "transport", "Remote-display ports", "Scan RDP, VNC, and X11 ports.", ("-sT",), "3389,5800,5900-5903,6000-6003"),
    profile("scan_tcp_devops_ports", "transport", "DevOps ports", "Scan common container, CI, metrics, and cluster ports.", ("-sT",), "2375,2376,6443,8001,8080,8443,9090,10250"),
    profile("scan_tcp_connect", "transport", "TCP connect", "Use operating-system TCP connect calls.", ("-sT",), "22,80,443,8000"),
    profile("scan_tcp_syn", "transport", "TCP SYN", "Use half-open TCP SYN scanning.", ("-sS",), "22,80,443,8000", risk="medium", elevated=True),
    profile("scan_tcp_ack", "firewall", "TCP ACK", "Map filtered versus unfiltered paths.", ("-sA",), "22,80,443", risk="medium", elevated=True),
    profile("scan_tcp_window", "firewall", "TCP window", "Study TCP window response behavior.", ("-sW",), "22,80,443", risk="medium", elevated=True),
    profile("scan_tcp_fin", "transport", "TCP FIN", "Compare TCP FIN response behavior.", ("-sF",), "22,80,443", risk="medium", elevated=True),
    profile("scan_tcp_null", "transport", "TCP NULL", "Compare TCP packets with no flags set.", ("-sN",), "22,80,443", risk="medium", elevated=True),
    profile("scan_tcp_xmas", "transport", "TCP Xmas", "Compare FIN, PSH, and URG response behavior.", ("-sX",), "22,80,443", risk="medium", elevated=True),
    profile("scan_tcp_maimon", "transport", "TCP Maimon", "Study FIN and ACK response behavior.", ("-sM",), "22,80,443", risk="medium", elevated=True),
    profile("scan_tcp_sequential", "transport", "Sequential TCP", "Scan selected ports in numeric order.", ("-sT", "-r"), "20-25,53,80,110,139,143,443,445"),
    profile("scan_tcp_no_ping", "transport", "Known-up TCP", "Skip discovery and scan a known-up host.", ("-sT", "-Pn", "--top-ports", "100"), risk="medium"),
    profile("scan_tcp_packet_trace", "diagnostics", "TCP packet trace", "Print packets for a tiny loopback scan.", ("-sT", "--packet-trace"), "2222,8000", scope="loopback", risk="high"),
    profile("scan_udp_common", "transport", "Common UDP", "Scan DNS, NTP, SNMP, IKE, and lab UDP ports.", ("-sU",), "53,123,161,500,5353", risk="medium", elevated=True),
    profile("scan_udp_top_20", "transport", "Top 20 UDP", "Scan 20 most common UDP ports.", ("-sU", "--top-ports", "20"), risk="medium", elevated=True),
    profile("scan_udp_top_100", "transport", "Top 100 UDP", "Scan 100 most common UDP ports.", ("-sU", "--top-ports", "100"), risk="medium", elevated=True),
    profile("scan_mixed_tcp_udp", "transport", "Mixed TCP and UDP", "Scan a small combined TCP and UDP set.", ("-sT", "-sU", "-p", "T:22,80,443,U:53,123,161"), risk="medium", elevated=True),
    profile("scan_sctp_init", "transport", "SCTP INIT", "Scan common SCTP ports using INIT packets.", ("-sY",), "80,2905,3868", risk="medium", elevated=True),
    profile("scan_sctp_cookie", "transport", "SCTP COOKIE", "Study SCTP COOKIE ECHO response behavior.", ("-sZ",), "80,2905,3868", risk="medium", elevated=True),
    profile("scan_ip_protocols", "transport", "IP protocols", "Identify supported IP protocols instead of ports.", ("-sO",), risk="medium", elevated=True),

    profile("scan_service_light", "service", "Light service detection", "Identify services with light probes.", ("-sT", "-sV", "--version-light", "--top-ports", "100")),
    profile("scan_service_default", "service", "Default service detection", "Identify services with default probes.", ("-sT", "-sV", "--top-ports", "100")),
    profile("scan_service_all", "service", "Full service detection", "Try every registered service probe.", ("-sT", "-sV", "--version-all", "--top-ports", "100"), risk="medium"),
    profile("scan_service_banner", "service", "Generic banners", "Collect generic banners from selected services.", ("-sT", "-sV", "--script", "banner"), "21,22,25,80,110,143,443,8000,9000"),
    profile("scan_scripts_default", "nse", "Default NSE", "Run Nmap default NSE scripts.", ("-sT", "-sV", "--script", "default", "--top-ports", "100"), risk="medium"),
    profile("scan_scripts_safe", "nse", "Safe NSE", "Run NSE scripts categorized safe.", ("-sT", "-sV", "--script", "safe", "--top-ports", "100"), risk="medium"),
    profile("scan_scripts_default_safe", "nse", "Default and safe NSE", "Run scripts in both default and safe sets.", ("-sT", "-sV", "--script", "default and safe", "--top-ports", "100")),
    profile("scan_os_fingerprint", "service", "OS fingerprint", "Attempt bounded OS fingerprinting.", ("-O", "--osscan-limit", "--max-os-tries", "1", "--top-ports", "1000"), risk="medium", elevated=True),
    profile("scan_os_guess", "service", "Aggressive OS guess", "Show OS guesses with bounded retries.", ("-O", "--osscan-guess", "--max-os-tries", "1", "--top-ports", "1000"), risk="medium", elevated=True),
    profile("scan_rpc", "service", "RPC service scan", "Identify RPC programs and versions.", ("-sT", "-sV", "-sR"), "111,135,593,2049", risk="medium"),
    profile("scan_aggressive_lab", "diagnostics", "Aggressive loopback", "Practice Nmap aggressive mode only on loopback.", ("-A",), "2222,8000,9000", scope="loopback", risk="high", elevated=True),
    profile("scan_script_trace_lab", "diagnostics", "NSE loopback trace", "Trace conservative NSE traffic against local lab.", ("-sT", "-sV", "--script", "default and safe", "--script-trace"), "2222,8000", scope="loopback", risk="high"),
)


# One bounded, informational NSE profile is created for every tuple below.
# Tuple: (script name, title, risk). Ports and transport come from family.
NSE_FAMILIES: dict[str, tuple[str, str, tuple[tuple[str, str, str], ...]]] = {
    "http": ("tcp:80,443,631,8000,8008,8080,8081,8443,8888", "HTTP", (
        ("http-title", "page titles", "low"), ("http-headers", "response headers", "low"),
        ("http-server-header", "server headers", "low"), ("http-security-headers", "security headers", "low"),
        ("http-methods", "supported methods", "medium"), ("http-robots.txt", "robots rules", "low"),
        ("http-favicon", "favicon fingerprints", "low"), ("http-generator", "generator metadata", "low"),
        ("http-cookie-flags", "cookie flags", "low"), ("http-cors", "CORS policy", "low"),
        ("http-date", "server date", "low"), ("http-auth", "authentication schemes", "low"),
        ("http-ntlm-info", "NTLM metadata", "low"), ("http-trace", "TRACE behavior", "medium"),
        ("http-webdav-scan", "WebDAV capabilities", "medium"), ("http-enum", "common application paths", "medium"),
        ("http-git", "exposed Git metadata", "medium"), ("http-comments-displayer", "HTML comments", "medium"),
        ("http-php-version", "PHP version clues", "low"), ("http-wordpress-enum", "WordPress metadata", "medium"),
    )),
    "tls": ("tcp:443,465,636,853,993,995,8443", "TLS", (
        ("ssl-cert", "certificate details", "low"), ("ssl-date", "service clock", "low"),
        ("ssl-enum-ciphers", "versions and ciphers", "medium"), ("ssl-dh-params", "DH parameters", "medium"),
        ("tls-alpn", "ALPN protocols", "low"), ("tls-nextprotoneg", "legacy next protocols", "low"),
        ("ssl-known-key", "known-key matches", "low"), ("ssl-cert-intaddr", "internal certificate addresses", "low"),
    )),
    "dns": ("udp:53", "DNS", (
        ("dns-nsid", "server identity", "low"), ("dns-recursion", "recursion behavior", "low"),
        ("dns-service-discovery", "service records", "medium"), ("dns-cache-snoop", "cache behavior", "medium"),
        ("dns-random-srcport", "source-port randomization", "medium"), ("dns-random-txid", "transaction-ID randomization", "medium"),
        ("dns-zone-transfer", "authorized zone transfer", "medium"),
    )),
    "ssh": ("tcp:22,2222", "SSH", (
        ("ssh-hostkey", "host-key fingerprints", "low"), ("ssh2-enum-algos", "protocol algorithms", "low"),
        ("ssh-auth-methods", "authentication methods", "medium"), ("sshv1", "obsolete protocol v1 support", "low"),
    )),
    "file-transfer": ("tcp:21", "FTP", (
        ("ftp-anon", "anonymous access", "medium"), ("ftp-syst", "platform response", "low"),
        ("ftp-bounce", "bounce behavior", "medium"),
    )),
    "mail": ("tcp:25,110,143,465,587,993,995", "Mail", (
        ("smtp-commands", "SMTP commands", "low"), ("smtp-ntlm-info", "SMTP NTLM metadata", "low"),
        ("smtp-strangeport", "SMTP on unusual ports", "low"), ("smtp-open-relay", "relay configuration", "medium"),
        ("imap-capabilities", "IMAP capabilities", "low"), ("imap-ntlm-info", "IMAP NTLM metadata", "low"),
        ("pop3-capabilities", "POP3 capabilities", "low"), ("pop3-ntlm-info", "POP3 NTLM metadata", "low"),
    )),
    "smb": ("tcp:139,445", "SMB", (
        ("smb-protocols", "protocol dialects", "low"), ("smb-security-mode", "signing and authentication mode", "low"),
        ("smb-os-discovery", "OS metadata", "low"), ("smb-system-info", "system information", "medium"),
        ("smb-enum-shares", "shares", "medium"), ("smb-enum-users", "users", "medium"),
        ("smb-enum-domains", "domains", "medium"), ("smb-enum-groups", "groups", "medium"),
        ("smb-enum-sessions", "sessions", "medium"), ("smb-enum-services", "services", "medium"),
        ("smb-server-stats", "server statistics", "medium"),
    )),
    "snmp": ("udp:161", "SNMP", (
        ("snmp-info", "system information", "low"), ("snmp-interfaces", "interfaces", "medium"),
        ("snmp-netstat", "network tables", "medium"), ("snmp-processes", "processes", "medium"),
        ("snmp-sysdescr", "system description", "low"), ("snmp-win32-services", "Windows services", "medium"),
        ("snmp-win32-software", "Windows software", "medium"),
    )),
    "database": ("tcp:523,1433,1521,3306,5984,6379,9042,9160,11211,27017", "Database", (
        ("mysql-info", "MySQL handshake", "low"), ("mysql-variables", "MySQL variables", "medium"),
        ("mysql-databases", "MySQL databases", "medium"), ("ms-sql-info", "MSSQL instances", "low"),
        ("ms-sql-ntlm-info", "MSSQL NTLM metadata", "low"), ("mongodb-info", "MongoDB information", "low"),
        ("mongodb-databases", "MongoDB databases", "medium"), ("redis-info", "Redis information", "low"),
        ("cassandra-info", "Cassandra information", "low"), ("couchdb-databases", "CouchDB databases", "medium"),
        ("couchdb-stats", "CouchDB statistics", "low"), ("memcached-info", "Memcached statistics", "low"),
        ("oracle-tns-version", "Oracle TNS version", "low"), ("db2-das-info", "DB2 information", "low"),
    )),
    "infrastructure": ("tcp:23,102,111,389,443,502,548,554,631,873,902,1099,1883,2049,2375,2376,2404,3260,3389,5005,5060,5061,5222,5269,5671,5672,5900-5903,6000-6003,6633,6653,6667,6697,8000,8333,8554,8883,18333,44818;udp:69,123,161,500,623,1900,3478,4500,5060,47808", "Infrastructure", (
        ("rdp-enum-encryption", "RDP encryption", "medium"), ("rdp-ntlm-info", "RDP NTLM metadata", "low"),
        ("vnc-info", "VNC protocol information", "low"), ("vnc-title", "VNC desktop title", "low"),
        ("x11-access", "X11 unauthenticated access", "medium"), ("nfs-showmount", "NFS exports", "medium"),
        ("nfs-statfs", "NFS filesystem statistics", "medium"), ("nfs-ls", "NFS export contents", "medium"),
        ("ntp-info", "NTP information", "low"), ("upnp-info", "UPnP device information", "low"),
        ("docker-version", "Docker API version", "low"), ("modbus-discover", "Modbus identification", "medium"),
        ("bacnet-info", "BACnet information", "medium"), ("enip-info", "EtherNet/IP information", "medium"),
        ("s7-info", "Siemens S7 information", "medium"), ("iec-identify", "IEC 104 identification", "medium"),
        ("mqtt-subscribe", "MQTT system topics", "medium"), ("amqp-info", "AMQP information", "low"),
        ("ldap-rootdse", "LDAP Root DSE", "low"), ("rsync-list-modules", "rsync modules", "low"),
        ("rtsp-methods", "RTSP methods", "low"), ("sip-methods", "SIP methods", "low"),
        ("telnet-encryption", "Telnet encryption", "low"), ("telnet-ntlm-info", "Telnet NTLM metadata", "low"),
        ("tftp-version", "TFTP version", "low"), ("ipmi-version", "IPMI version", "low"),
        ("iscsi-info", "iSCSI target information", "low"), ("rmi-dumpregistry", "RMI bindings", "medium"),
        ("jdwp-info", "JDWP information", "low"), ("afp-serverinfo", "AFP information", "low"),
        ("cups-info", "CUPS information", "low"), ("cups-queue-info", "CUPS queues", "medium"),
        ("ike-version", "IKE version", "low"), ("stun-info", "STUN information", "low"),
        ("xmpp-info", "XMPP features", "low"), ("irc-info", "IRC information", "low"),
        ("bitcoin-info", "Bitcoin peer information", "low"), ("openflow-info", "OpenFlow information", "low"),
        ("vmware-version", "VMware version", "low"),
    )),
}


NSE_UDP_SCRIPTS = {
    "dns-nsid", "dns-recursion", "dns-service-discovery", "dns-cache-snoop",
    "dns-random-srcport", "dns-random-txid", "dns-zone-transfer",
    "snmp-info", "snmp-interfaces", "snmp-netstat", "snmp-processes",
    "snmp-sysdescr", "snmp-win32-services", "snmp-win32-software",
    "ntp-info", "upnp-info", "bacnet-info", "sip-methods", "tftp-version",
    "ipmi-version", "ike-version", "stun-info",
}


# Families keep registry compact; overrides keep each protocol script narrow.
NSE_PORT_OVERRIDES = {
    "smtp-commands": "25,465,587", "smtp-ntlm-info": "25,465,587",
    "smtp-strangeport": "25,465,587,2525", "smtp-open-relay": "25,465,587",
    "imap-capabilities": "143,993", "imap-ntlm-info": "143,993",
    "pop3-capabilities": "110,995", "pop3-ntlm-info": "110,995",
    "mysql-info": "3306", "mysql-variables": "3306", "mysql-databases": "3306",
    "ms-sql-info": "1433", "ms-sql-ntlm-info": "1433",
    "mongodb-info": "27017", "mongodb-databases": "27017", "redis-info": "6379",
    "cassandra-info": "9042,9160", "couchdb-databases": "5984", "couchdb-stats": "5984",
    "memcached-info": "11211", "oracle-tns-version": "1521", "db2-das-info": "523",
    "rdp-enum-encryption": "3389", "rdp-ntlm-info": "3389",
    "vnc-info": "5900-5903", "vnc-title": "5900-5903", "x11-access": "6000-6003",
    "nfs-showmount": "111,2049", "nfs-statfs": "111,2049", "nfs-ls": "111,2049",
    "ntp-info": "123", "upnp-info": "1900,5000", "docker-version": "2375,2376",
    "modbus-discover": "502", "bacnet-info": "47808", "enip-info": "44818",
    "s7-info": "102", "iec-identify": "2404", "mqtt-subscribe": "1883,8883",
    "amqp-info": "5671,5672", "ldap-rootdse": "389,636", "rsync-list-modules": "873",
    "rtsp-methods": "554,8554", "sip-methods": "5060,5061", "telnet-encryption": "23",
    "telnet-ntlm-info": "23", "tftp-version": "69", "ipmi-version": "623",
    "iscsi-info": "3260", "rmi-dumpregistry": "1099", "jdwp-info": "5005,8000",
    "afp-serverinfo": "548", "cups-info": "631", "cups-queue-info": "631",
    "ike-version": "500,4500", "stun-info": "3478", "xmpp-info": "5222,5269",
    "irc-info": "6667,6697", "bitcoin-info": "8333,18333",
    "openflow-info": "6633,6653", "vmware-version": "443,902",
}


def nse_rows() -> tuple[ScanProfile, ...]:
    rows: list[ScanProfile] = []
    for category, (port_spec, family_title, scripts) in NSE_FAMILIES.items():
        # Most families use one transport. Infrastructure intentionally mixes
        # TCP and UDP, so split both port sets and select per NSE script.
        port_sets = dict(item.split(":", 1) for item in port_spec.split(";"))
        for script_name, purpose, risk in scripts:
            transport = "udp" if script_name in NSE_UDP_SCRIPTS else "tcp"
            ports = NSE_PORT_OVERRIDES.get(
                script_name, port_sets.get(transport) or next(iter(port_sets.values()))
            )
            scan_type = "-sU" if transport == "udp" else "-sT"
            elevated = transport == "udp"
            safe_name = script_name.replace("-", "_").replace(".", "_")
            rows.append(profile(
                f"scan_{safe_name}", category, f"{family_title}: {purpose}",
                f"Run bounded {script_name} NSE checks for {purpose} on authorized services.",
                (scan_type, "-sV", "--version-light", "--script", script_name,
                 "--script-timeout", "30s", "--host-timeout", "5m", "--open"),
                ports, risk=risk, elevated=elevated,
            ))
    return tuple(rows)


def build_registry(rows: tuple[ScanProfile, ...]) -> dict[str, ScanProfile]:
    registry: dict[str, ScanProfile] = {}
    for item in rows:
        if item.name in registry:
            raise ValueError(f"Duplicate profile name: {item.name}")
        if item.scope not in {"authorized", "private", "loopback"}:
            raise ValueError(f"Invalid scope for {item.name}: {item.scope}")
        if item.risk not in {"low", "medium", "high"}:
            raise ValueError(f"Invalid risk for {item.name}: {item.risk}")
        registry[item.name] = item
    return registry


_base_rows = CORE_ROWS + nse_rows()
_base_names = {item.name for item in _base_rows}
_extra_rows = tuple(
    profile(
        item["name"], item["category"], item["title"], item["description"],
        tuple(item["arguments"]), item["default_ports"], item["scope"],
        item["risk"], item["elevated"], item["timing"],
    )
    for item in EXTRA_PROFILE_DATA
    if item["name"] not in _base_names
)
# Extra high-impact techniques stay loopback-only even if data row was looser.
_extra_rows = tuple(
    profile(
        item.name, item.category, item.title, item.description, item.arguments,
        item.default_ports, "loopback" if item.risk == "high" else item.scope,
        item.risk, item.elevated, item.timing,
    )
    for item in _extra_rows
)
PROFILE_ROWS = _base_rows + _extra_rows
PROFILES = build_registry(PROFILE_ROWS)
