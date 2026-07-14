# Complete profile catalog

Generated from live registry. Contains **358 profiles**. Each script
accepts shared options documented in [script guide](script-guide.md). Use
`profile_catalog.py` for interactive search and filtering.

```bash
python3 scripts/profile_catalog.py --search tls
python3 scripts/profile_catalog.py --category discovery --risk low
```

## Risk and scope

- `low`: narrow discovery or information retrieval.
- `medium`: broader, raw-packet, enumeration, or higher-traffic behavior.
- `high`: loopback-only experiments enforced by runner.
- `authorized`: private targets work directly; public/unresolved targets need explicit opt-in.
- `private`: only private, link-local, or loopback targets.
- `loopback`: only localhost, `127.0.0.0/8`, or `::1`.

## data (14)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_ajp_headers.py` | AJP headers | low | authorized | no | `8009` | `-sT -sV --version-light --script ajp-headers --script-timeout 30s --open` |
| `scan_ajp_methods.py` | AJP methods | medium | private | no | `8009` | `-sT -sV --version-light --script ajp-methods --script-timeout 30s --open` |
| `scan_bitcoin_peers.py` | Bitcoin peer addresses | medium | private | no | `8333,18333` | `-sT -sV --version-light --script bitcoin-getaddr --script-timeout 30s --open` |
| `scan_bittorrent_discovery.py` | BitTorrent discovery | medium | private | no | `6881-6889` | `-sT -sV --version-light --script bittorrent-discovery --script-timeout 30s --open` |
| `scan_epmd_info.py` | Erlang EPMD information | low | authorized | no | `4369` | `-sT -sV --version-light --script epmd-info --script-timeout 30s --open` |
| `scan_hadoop_datanode.py` | Hadoop DataNode | low | authorized | no | `50075,9864` | `-sT -sV --version-light --script hadoop-datanode-info --script-timeout 30s --open` |
| `scan_hadoop_jobtracker.py` | Hadoop JobTracker | low | authorized | no | `50030` | `-sT -sV --version-light --script hadoop-jobtracker-info --script-timeout 30s --open` |
| `scan_hadoop_namenode.py` | Hadoop NameNode | low | authorized | no | `50070,9870` | `-sT -sV --version-light --script hadoop-namenode-info --script-timeout 30s --open` |
| `scan_hadoop_secondary.py` | Hadoop secondary NameNode | low | authorized | no | `50090,9868` | `-sT -sV --version-light --script hadoop-secondary-namenode-info --script-timeout 30s --open` |
| `scan_hadoop_tasktracker.py` | Hadoop TaskTracker | low | authorized | no | `50060` | `-sT -sV --version-light --script hadoop-tasktracker-info --script-timeout 30s --open` |
| `scan_mqtt_subscribe_private.py` | MQTT subscription sample | medium | private | no | `1883,8883` | `-sT -sV --version-light --script mqtt-subscribe --script-timeout 30s --open` |
| `scan_mssql_info.py` | Microsoft SQL information | low | authorized | no | `1433` | `-sT -sV --version-light --script ms-sql-info --script-timeout 30s --open` |
| `scan_mssql_ntlm.py` | Microsoft SQL NTLM metadata | low | authorized | no | `1433` | `-sT -sV --version-light --script ms-sql-ntlm-info --script-timeout 30s --open` |
| `scan_mysql_empty_password.py` | MySQL empty password | medium | private | no | `3306` | `-sT -sV --version-light --script mysql-empty-password --script-timeout 30s --open` |

## database (14)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_cassandra_info.py` | Database: Cassandra information | low | authorized | no | `9042,9160` | `-sT -sV --version-light --script cassandra-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_couchdb_databases.py` | Database: CouchDB databases | medium | authorized | no | `5984` | `-sT -sV --version-light --script couchdb-databases --script-timeout 30s --host-timeout 5m --open` |
| `scan_couchdb_stats.py` | Database: CouchDB statistics | low | authorized | no | `5984` | `-sT -sV --version-light --script couchdb-stats --script-timeout 30s --host-timeout 5m --open` |
| `scan_db2_das_info.py` | Database: DB2 information | low | authorized | no | `523` | `-sT -sV --version-light --script db2-das-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_memcached_info.py` | Database: Memcached statistics | low | authorized | no | `11211` | `-sT -sV --version-light --script memcached-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_mongodb_databases.py` | Database: MongoDB databases | medium | authorized | no | `27017` | `-sT -sV --version-light --script mongodb-databases --script-timeout 30s --host-timeout 5m --open` |
| `scan_mongodb_info.py` | Database: MongoDB information | low | authorized | no | `27017` | `-sT -sV --version-light --script mongodb-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_ms_sql_info.py` | Database: MSSQL instances | low | authorized | no | `1433` | `-sT -sV --version-light --script ms-sql-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_ms_sql_ntlm_info.py` | Database: MSSQL NTLM metadata | low | authorized | no | `1433` | `-sT -sV --version-light --script ms-sql-ntlm-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_mysql_databases.py` | Database: MySQL databases | medium | authorized | no | `3306` | `-sT -sV --version-light --script mysql-databases --script-timeout 30s --host-timeout 5m --open` |
| `scan_mysql_info.py` | Database: MySQL handshake | low | authorized | no | `3306` | `-sT -sV --version-light --script mysql-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_mysql_variables.py` | Database: MySQL variables | medium | authorized | no | `3306` | `-sT -sV --version-light --script mysql-variables --script-timeout 30s --host-timeout 5m --open` |
| `scan_oracle_tns_version.py` | Database: Oracle TNS version | low | authorized | no | `1521` | `-sT -sV --version-light --script oracle-tns-version --script-timeout 30s --host-timeout 5m --open` |
| `scan_redis_info.py` | Database: Redis information | low | authorized | no | `6379` | `-sT -sV --version-light --script redis-info --script-timeout 30s --host-timeout 5m --open` |

## diagnostics (3)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_aggressive_lab.py` | Aggressive loopback | high | loopback | yes | `2222,8000,9000` | `-A` |
| `scan_script_trace_lab.py` | NSE loopback trace | high | loopback | no | `2222,8000` | `-sT -sV --script default and safe --script-trace` |
| `scan_tcp_packet_trace.py` | TCP packet trace | high | loopback | no | `2222,8000` | `-sT --packet-trace` |

## discovery (38)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_discover_ack.py` | ACK discovery | low | private | yes | — | `-sn -PA22,80,443` |
| `scan_discover_arp.py` | ARP discovery | low | private | yes | — | `-sn -PR` |
| `scan_discover_default.py` | Default discovery | low | private | no | — | `-sn` |
| `scan_discover_icmp_combo.py` | Combined ICMP discovery | low | private | yes | — | `-sn -PE -PP -PM` |
| `scan_discover_icmp_echo.py` | ICMP echo discovery | low | private | yes | — | `-sn -PE` |
| `scan_discover_icmp_mask.py` | ICMP mask discovery | low | private | yes | — | `-sn -PM` |
| `scan_discover_icmp_timestamp.py` | ICMP timestamp discovery | low | private | yes | — | `-sn -PP` |
| `scan_discover_ip_protocol.py` | IP protocol discovery | low | private | yes | — | `-sn -PO1,2,4` |
| `scan_discover_ipv6.py` | IPv6 discovery | low | authorized | no | — | `-6 -sn` |
| `scan_discover_no_dns.py` | Discovery without DNS | low | private | no | — | `-sn -n` |
| `scan_discover_sctp.py` | SCTP discovery | low | private | yes | — | `-sn -PY80,2905` |
| `scan_discover_syn_common.py` | Common-port SYN discovery | low | private | yes | — | `-sn -PS22,80,443` |
| `scan_discover_syn_web.py` | Web-port SYN discovery | low | private | yes | — | `-sn -PS80,443,8000,8080,8443` |
| `scan_discover_traceroute.py` | Discovery traceroute | low | authorized | no | — | `-sn --traceroute` |
| `scan_discover_udp.py` | UDP discovery | low | private | yes | — | `-sn -PU53,123,161` |
| `scan_discover_verbose.py` | Verbose discovery | low | private | no | — | `-sn -vv --reason` |
| `scan_discovery_arp.py` | ARP discovery | low | private | yes | — | `-sn -PR --reason` |
| `scan_discovery_combined.py` | Combined host discovery | medium | authorized | yes | — | `-sn -PE -PS22,80,443 -PA80,443 -PU53,123 --reason` |
| `scan_discovery_default_profile.py` | Default host discovery | low | authorized | no | — | `-sn --reason` |
| `scan_discovery_fast_private.py` | Faster private discovery | medium | private | no | — | `-sn --reason` |
| `scan_discovery_force_dns.py` | Host discovery with DNS | low | authorized | no | — | `-sn -R --reason` |
| `scan_discovery_icmp_echo.py` | ICMP echo discovery | low | authorized | yes | — | `-sn -PE --reason` |
| `scan_discovery_icmp_netmask.py` | ICMP netmask discovery | low | private | yes | — | `-sn -PM --reason` |
| `scan_discovery_icmp_timestamp.py` | ICMP timestamp discovery | low | authorized | yes | — | `-sn -PP --reason` |
| `scan_discovery_ip_protocols.py` | IP protocol discovery | medium | authorized | yes | — | `-sn -PO1,2,4,6,17 --reason` |
| `scan_discovery_ipv6.py` | IPv6 host discovery | low | authorized | yes | — | `-6 -sn --reason` |
| `scan_discovery_no_dns.py` | Host discovery without DNS | low | authorized | no | — | `-sn -n --reason` |
| `scan_discovery_sctp.py` | SCTP discovery | medium | authorized | yes | — | `-sn -PY80,443,3868 --reason` |
| `scan_discovery_tcp_ack_common.py` | TCP ACK discovery | low | authorized | yes | — | `-sn -PA22,80,443 --reason` |
| `scan_discovery_tcp_syn_common.py` | TCP SYN discovery | low | authorized | yes | — | `-sn -PS22,80,443 --reason` |
| `scan_discovery_tcp_syn_web.py` | Web-port SYN discovery | low | authorized | yes | — | `-sn -PS80,443,8000,8080,8443 --reason` |
| `scan_discovery_traceroute.py` | Discovery with traceroute | low | authorized | no | — | `-sn --traceroute --reason` |
| `scan_discovery_udp_common.py` | UDP discovery | low | authorized | yes | — | `-sn -PU53,67,68,123,161 --reason` |
| `scan_discovery_verbose_reasons.py` | Verbose discovery reasons | low | authorized | no | — | `-sn --reason -vv` |
| `scan_list_targets.py` | List targets | low | private | no | — | `-sL` |
| `scan_list_targets_dns.py` | List targets with DNS | low | private | no | — | `-sL -R` |
| `scan_list_targets_no_dns.py` | List targets without DNS | low | authorized | no | — | `-sL -n` |
| `scan_list_targets_with_dns.py` | List targets with DNS | low | authorized | no | — | `-sL -R` |

## dns (7)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_dns_cache_snoop.py` | DNS: cache behavior | medium | authorized | yes | `53` | `-sU -sV --version-light --script dns-cache-snoop --script-timeout 30s --host-timeout 5m --open` |
| `scan_dns_nsid.py` | DNS: server identity | low | authorized | yes | `53` | `-sU -sV --version-light --script dns-nsid --script-timeout 30s --host-timeout 5m --open` |
| `scan_dns_random_srcport.py` | DNS: source-port randomization | medium | authorized | yes | `53` | `-sU -sV --version-light --script dns-random-srcport --script-timeout 30s --host-timeout 5m --open` |
| `scan_dns_random_txid.py` | DNS: transaction-ID randomization | medium | authorized | yes | `53` | `-sU -sV --version-light --script dns-random-txid --script-timeout 30s --host-timeout 5m --open` |
| `scan_dns_recursion.py` | DNS: recursion behavior | low | authorized | yes | `53` | `-sU -sV --version-light --script dns-recursion --script-timeout 30s --host-timeout 5m --open` |
| `scan_dns_service_discovery.py` | DNS: service records | medium | authorized | yes | `53` | `-sU -sV --version-light --script dns-service-discovery --script-timeout 30s --host-timeout 5m --open` |
| `scan_dns_zone_transfer.py` | DNS: authorized zone transfer | medium | authorized | yes | `53` | `-sU -sV --version-light --script dns-zone-transfer --script-timeout 30s --host-timeout 5m --open` |

## file-transfer (3)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_ftp_anon.py` | FTP: anonymous access | medium | authorized | no | `21` | `-sT -sV --version-light --script ftp-anon --script-timeout 30s --host-timeout 5m --open` |
| `scan_ftp_bounce.py` | FTP: bounce behavior | medium | authorized | no | `21` | `-sT -sV --version-light --script ftp-bounce --script-timeout 30s --host-timeout 5m --open` |
| `scan_ftp_syst.py` | FTP: platform response | low | authorized | no | `21` | `-sT -sV --version-light --script ftp-syst --script-timeout 30s --host-timeout 5m --open` |

## firewall (2)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_tcp_ack.py` | TCP ACK | medium | authorized | yes | `22,80,443` | `-sA` |
| `scan_tcp_window.py` | TCP window | medium | authorized | yes | `22,80,443` | `-sW` |

## http (20)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_http_auth.py` | HTTP: authentication schemes | low | authorized | no | `80,443,631,8000,8008,8080,8081,8443,8888` | `-sT -sV --version-light --script http-auth --script-timeout 30s --host-timeout 5m --open` |
| `scan_http_comments_displayer.py` | HTTP: HTML comments | medium | authorized | no | `80,443,631,8000,8008,8080,8081,8443,8888` | `-sT -sV --version-light --script http-comments-displayer --script-timeout 30s --host-timeout 5m --open` |
| `scan_http_cookie_flags.py` | HTTP: cookie flags | low | authorized | no | `80,443,631,8000,8008,8080,8081,8443,8888` | `-sT -sV --version-light --script http-cookie-flags --script-timeout 30s --host-timeout 5m --open` |
| `scan_http_cors.py` | HTTP: CORS policy | low | authorized | no | `80,443,631,8000,8008,8080,8081,8443,8888` | `-sT -sV --version-light --script http-cors --script-timeout 30s --host-timeout 5m --open` |
| `scan_http_date.py` | HTTP: server date | low | authorized | no | `80,443,631,8000,8008,8080,8081,8443,8888` | `-sT -sV --version-light --script http-date --script-timeout 30s --host-timeout 5m --open` |
| `scan_http_enum.py` | HTTP: common application paths | medium | authorized | no | `80,443,631,8000,8008,8080,8081,8443,8888` | `-sT -sV --version-light --script http-enum --script-timeout 30s --host-timeout 5m --open` |
| `scan_http_favicon.py` | HTTP: favicon fingerprints | low | authorized | no | `80,443,631,8000,8008,8080,8081,8443,8888` | `-sT -sV --version-light --script http-favicon --script-timeout 30s --host-timeout 5m --open` |
| `scan_http_generator.py` | HTTP: generator metadata | low | authorized | no | `80,443,631,8000,8008,8080,8081,8443,8888` | `-sT -sV --version-light --script http-generator --script-timeout 30s --host-timeout 5m --open` |
| `scan_http_git.py` | HTTP: exposed Git metadata | medium | authorized | no | `80,443,631,8000,8008,8080,8081,8443,8888` | `-sT -sV --version-light --script http-git --script-timeout 30s --host-timeout 5m --open` |
| `scan_http_headers.py` | HTTP: response headers | low | authorized | no | `80,443,631,8000,8008,8080,8081,8443,8888` | `-sT -sV --version-light --script http-headers --script-timeout 30s --host-timeout 5m --open` |
| `scan_http_methods.py` | HTTP: supported methods | medium | authorized | no | `80,443,631,8000,8008,8080,8081,8443,8888` | `-sT -sV --version-light --script http-methods --script-timeout 30s --host-timeout 5m --open` |
| `scan_http_ntlm_info.py` | HTTP: NTLM metadata | low | authorized | no | `80,443,631,8000,8008,8080,8081,8443,8888` | `-sT -sV --version-light --script http-ntlm-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_http_php_version.py` | HTTP: PHP version clues | low | authorized | no | `80,443,631,8000,8008,8080,8081,8443,8888` | `-sT -sV --version-light --script http-php-version --script-timeout 30s --host-timeout 5m --open` |
| `scan_http_robots_txt.py` | HTTP: robots rules | low | authorized | no | `80,443,631,8000,8008,8080,8081,8443,8888` | `-sT -sV --version-light --script http-robots.txt --script-timeout 30s --host-timeout 5m --open` |
| `scan_http_security_headers.py` | HTTP: security headers | low | authorized | no | `80,443,631,8000,8008,8080,8081,8443,8888` | `-sT -sV --version-light --script http-security-headers --script-timeout 30s --host-timeout 5m --open` |
| `scan_http_server_header.py` | HTTP: server headers | low | authorized | no | `80,443,631,8000,8008,8080,8081,8443,8888` | `-sT -sV --version-light --script http-server-header --script-timeout 30s --host-timeout 5m --open` |
| `scan_http_title.py` | HTTP: page titles | low | authorized | no | `80,443,631,8000,8008,8080,8081,8443,8888` | `-sT -sV --version-light --script http-title --script-timeout 30s --host-timeout 5m --open` |
| `scan_http_trace.py` | HTTP: TRACE behavior | medium | authorized | no | `80,443,631,8000,8008,8080,8081,8443,8888` | `-sT -sV --version-light --script http-trace --script-timeout 30s --host-timeout 5m --open` |
| `scan_http_webdav_scan.py` | HTTP: WebDAV capabilities | medium | authorized | no | `80,443,631,8000,8008,8080,8081,8443,8888` | `-sT -sV --version-light --script http-webdav-scan --script-timeout 30s --host-timeout 5m --open` |
| `scan_http_wordpress_enum.py` | HTTP: WordPress metadata | medium | authorized | no | `80,443,631,8000,8008,8080,8081,8443,8888` | `-sT -sV --version-light --script http-wordpress-enum --script-timeout 30s --host-timeout 5m --open` |

## infrastructure (52)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_afp_serverinfo.py` | Infrastructure: AFP information | low | authorized | no | `548` | `-sT -sV --version-light --script afp-serverinfo --script-timeout 30s --host-timeout 5m --open` |
| `scan_amqp_info.py` | Infrastructure: AMQP information | low | authorized | no | `5671,5672` | `-sT -sV --version-light --script amqp-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_bacnet_info.py` | Infrastructure: BACnet information | medium | authorized | yes | `47808` | `-sU -sV --version-light --script bacnet-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_bitcoin_info.py` | Infrastructure: Bitcoin peer information | low | authorized | no | `8333,18333` | `-sT -sV --version-light --script bitcoin-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_bjnp_printer.py` | Canon BJNP discovery | medium | private | yes | `8611-8614` | `-sU -sV --version-light --script bjnp-discover --script-timeout 30s --open` |
| `scan_coap_resources.py` | CoAP resources | medium | private | yes | `5683,5684` | `-sU -sV --version-light --script coap-resources --script-timeout 30s --open` |
| `scan_cups_info.py` | Infrastructure: CUPS information | low | authorized | no | `631` | `-sT -sV --version-light --script cups-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_cups_queue_info.py` | Infrastructure: CUPS queues | medium | authorized | no | `631` | `-sT -sV --version-light --script cups-queue-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_cups_queues.py` | CUPS queues | medium | private | no | `631` | `-sT -sV --version-light --script cups-queue-info --script-timeout 30s --open` |
| `scan_daytime_info.py` | Daytime service | low | authorized | no | `13` | `-sT -sV --version-light --script daytime --script-timeout 30s --open` |
| `scan_dns_source_port.py` | DNS source-port randomness | low | authorized | yes | `53` | `-sU -sV --version-light --script dns-random-srcport --script-timeout 30s --open` |
| `scan_dns_srv_records.py` | DNS SRV records | medium | private | no | `53` | `-sT -sV --version-light --script dns-srv-enum --script-timeout 30s --open` |
| `scan_dns_transaction_id.py` | DNS transaction-ID randomness | low | authorized | yes | `53` | `-sU -sV --version-light --script dns-random-txid --script-timeout 30s --open` |
| `scan_dns_zone_check.py` | DNS zone consistency | medium | private | no | `53` | `-sT -sV --version-light --script dns-check-zone --script-timeout 30s --open` |
| `scan_docker_version.py` | Infrastructure: Docker API version | low | authorized | no | `2375,2376` | `-sT -sV --version-light --script docker-version --script-timeout 30s --host-timeout 5m --open` |
| `scan_enip_info.py` | Infrastructure: EtherNet/IP information | medium | authorized | no | `44818` | `-sT -sV --version-light --script enip-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_finger_info.py` | Finger service | low | authorized | no | `79` | `-sT -sV --version-light --script finger --script-timeout 30s --open` |
| `scan_gopher_listing.py` | Gopher listing | low | authorized | no | `70` | `-sT -sV --version-light --script gopher-ls --script-timeout 30s --open` |
| `scan_iec_identify.py` | Infrastructure: IEC 104 identification | medium | authorized | no | `2404` | `-sT -sV --version-light --script iec-identify --script-timeout 30s --host-timeout 5m --open` |
| `scan_ike_version.py` | Infrastructure: IKE version | low | authorized | yes | `500,4500` | `-sU -sV --version-light --script ike-version --script-timeout 30s --host-timeout 5m --open` |
| `scan_ipmi_version.py` | Infrastructure: IPMI version | low | authorized | yes | `623` | `-sU -sV --version-light --script ipmi-version --script-timeout 30s --host-timeout 5m --open` |
| `scan_irc_info.py` | Infrastructure: IRC information | low | authorized | no | `6667,6697` | `-sT -sV --version-light --script irc-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_iscsi_info.py` | Infrastructure: iSCSI target information | low | authorized | no | `3260` | `-sT -sV --version-light --script iscsi-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_jdwp_info.py` | Infrastructure: JDWP information | low | authorized | no | `5005,8000` | `-sT -sV --version-light --script jdwp-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_ldap_rootdse.py` | Infrastructure: LDAP Root DSE | low | authorized | no | `389,636` | `-sT -sV --version-light --script ldap-rootdse --script-timeout 30s --host-timeout 5m --open` |
| `scan_modbus_discover.py` | Infrastructure: Modbus identification | medium | authorized | no | `502` | `-sT -sV --version-light --script modbus-discover --script-timeout 30s --host-timeout 5m --open` |
| `scan_modbus_discovery.py` | Modbus discovery | medium | private | no | `502` | `-sT -sV --version-light --script modbus-discover --script-timeout 30s --open` |
| `scan_mqtt_subscribe.py` | Infrastructure: MQTT system topics | medium | authorized | no | `1883,8883` | `-sT -sV --version-light --script mqtt-subscribe --script-timeout 30s --host-timeout 5m --open` |
| `scan_nfs_ls.py` | Infrastructure: NFS export contents | medium | authorized | no | `111,2049` | `-sT -sV --version-light --script nfs-ls --script-timeout 30s --host-timeout 5m --open` |
| `scan_nfs_showmount.py` | Infrastructure: NFS exports | medium | authorized | no | `111,2049` | `-sT -sV --version-light --script nfs-showmount --script-timeout 30s --host-timeout 5m --open` |
| `scan_nfs_statfs.py` | Infrastructure: NFS filesystem statistics | medium | authorized | no | `111,2049` | `-sT -sV --version-light --script nfs-statfs --script-timeout 30s --host-timeout 5m --open` |
| `scan_ntp_info.py` | Infrastructure: NTP information | low | authorized | yes | `123` | `-sU -sV --version-light --script ntp-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_ntp_monlist_private.py` | NTP monitor list | medium | private | yes | `123` | `-sU -sV --version-light --script ntp-monlist --script-timeout 30s --open` |
| `scan_openflow_info.py` | Infrastructure: OpenFlow information | low | authorized | no | `6633,6653` | `-sT -sV --version-light --script openflow-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_rdp_enum_encryption.py` | Infrastructure: RDP encryption | medium | authorized | no | `3389` | `-sT -sV --version-light --script rdp-enum-encryption --script-timeout 30s --host-timeout 5m --open` |
| `scan_rdp_ntlm_info.py` | Infrastructure: RDP NTLM metadata | low | authorized | no | `3389` | `-sT -sV --version-light --script rdp-ntlm-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_rmi_dumpregistry.py` | Infrastructure: RMI bindings | medium | authorized | no | `1099` | `-sT -sV --version-light --script rmi-dumpregistry --script-timeout 30s --host-timeout 5m --open` |
| `scan_rsync_list_modules.py` | Infrastructure: rsync modules | low | authorized | no | `873` | `-sT -sV --version-light --script rsync-list-modules --script-timeout 30s --host-timeout 5m --open` |
| `scan_rtsp_methods.py` | Infrastructure: RTSP methods | low | authorized | no | `554,8554` | `-sT -sV --version-light --script rtsp-methods --script-timeout 30s --host-timeout 5m --open` |
| `scan_s7_info.py` | Infrastructure: Siemens S7 information | medium | authorized | no | `102` | `-sT -sV --version-light --script s7-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_sip_methods.py` | Infrastructure: SIP methods | low | authorized | yes | `5060,5061` | `-sU -sV --version-light --script sip-methods --script-timeout 30s --host-timeout 5m --open` |
| `scan_snmp_description.py` | SNMP system description | low | authorized | yes | `161` | `-sU -sV --version-light --script snmp-sysdescr --script-timeout 30s --open` |
| `scan_stun_info.py` | Infrastructure: STUN information | low | authorized | yes | `3478` | `-sU -sV --version-light --script stun-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_telnet_encryption.py` | Infrastructure: Telnet encryption | low | authorized | no | `23` | `-sT -sV --version-light --script telnet-encryption --script-timeout 30s --host-timeout 5m --open` |
| `scan_telnet_ntlm_info.py` | Infrastructure: Telnet NTLM metadata | low | authorized | no | `23` | `-sT -sV --version-light --script telnet-ntlm-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_tftp_version.py` | Infrastructure: TFTP version | low | authorized | yes | `69` | `-sU -sV --version-light --script tftp-version --script-timeout 30s --host-timeout 5m --open` |
| `scan_upnp_info.py` | Infrastructure: UPnP device information | low | authorized | yes | `1900,5000` | `-sU -sV --version-light --script upnp-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_vmware_version.py` | Infrastructure: VMware version | low | authorized | no | `443,902` | `-sT -sV --version-light --script vmware-version --script-timeout 30s --host-timeout 5m --open` |
| `scan_vnc_info.py` | Infrastructure: VNC protocol information | low | authorized | no | `5900-5903` | `-sT -sV --version-light --script vnc-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_vnc_title.py` | Infrastructure: VNC desktop title | low | authorized | no | `5900-5903` | `-sT -sV --version-light --script vnc-title --script-timeout 30s --host-timeout 5m --open` |
| `scan_x11_access.py` | Infrastructure: X11 unauthenticated access | medium | authorized | no | `6000-6003` | `-sT -sV --version-light --script x11-access --script-timeout 30s --host-timeout 5m --open` |
| `scan_xmpp_info.py` | Infrastructure: XMPP features | low | authorized | no | `5222,5269` | `-sT -sV --version-light --script xmpp-info --script-timeout 30s --host-timeout 5m --open` |

## inventory (18)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_backup_ports.py` | Backup service ports | low | authorized | no | `873,9101-9103,10000,13720-13724` | `-sT -sV --version-light --reason --open` |
| `scan_ci_cd_ports.py` | CI/CD service ports | low | authorized | no | `3000,8080,8081,9000,9090,9418` | `-sT -sV --version-light --reason --open` |
| `scan_container_apis.py` | Container and orchestration APIs | low | authorized | no | `2375,2376,4243,6443,8001,10250,10255` | `-sT -sV --version-light --reason --open` |
| `scan_database_ports.py` | Database service ports | low | authorized | no | `1433,1521,3306,5432,5984,6379,9042,9200,27017` | `-sT -sV --version-light --reason --open` |
| `scan_dev_servers.py` | Development servers | low | authorized | no | `3000,3001,4000,4200,5000,5173,8000,8080,8081,8888` | `-sT -sV --version-light --reason --open` |
| `scan_directory_service_ports.py` | Directory service ports | low | authorized | no | `389,636,3268,3269` | `-sT -sV --version-light --reason --open` |
| `scan_file_service_ports.py` | File service ports | low | authorized | no | `20,21,69,111,139,445,873,2049` | `-sT -sV --version-light --reason --open` |
| `scan_game_server_ports.py` | Common game server ports | low | authorized | no | `25565,27015-27020,27960,28015,30120` | `-sT -sV --version-light --reason --open` |
| `scan_iot_ports.py` | Common IoT service ports | low | authorized | no | `80,443,1883,5683,5684,8080,8883,10001,49152` | `-sT -sV --version-light --reason --open` |
| `scan_linux_service_ports.py` | Linux service ports | low | authorized | no | `22,25,53,80,111,123,443,631,873,2049,3306,5432` | `-sT -sV --version-light --reason --open` |
| `scan_mail_service_ports.py` | Mail service ports | low | authorized | no | `25,110,143,465,587,993,995` | `-sT -sV --version-light --reason --open` |
| `scan_message_queue_ports.py` | Message queue ports | low | authorized | no | `1883,4369,5671,5672,61613,61616,9092,15672` | `-sT -sV --version-light --reason --open` |
| `scan_monitoring_ports.py` | Monitoring service ports | low | authorized | no | `161,162,199,5666,10050,10051,3000,9090` | `-sT -sV --version-light --reason --open` |
| `scan_printer_ports.py` | Printer service ports | low | authorized | no | `515,631,9100,8611-8614` | `-sT -sV --version-light --reason --open` |
| `scan_remote_admin_ports.py` | Remote administration ports | low | authorized | no | `22,23,3389,5900-5903,5985,5986` | `-sT -sV --version-light --reason --open` |
| `scan_virtualization_ports.py` | Virtualization management ports | low | authorized | no | `443,902,903,16509,16514,8006` | `-sT -sV --version-light --reason --open` |
| `scan_voip_ports.py` | VoIP service ports | low | authorized | no | `1720,2000,2427,2727,5060,5061,4569` | `-sT -sV --version-light --reason --open` |
| `scan_windows_service_ports.py` | Windows service ports | low | authorized | no | `53,88,135,137-139,389,445,464,593,636,3268,3269,3389,5985,5986` | `-sT -sV --version-light --reason --open` |

## mail (8)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_imap_capabilities.py` | Mail: IMAP capabilities | low | authorized | no | `143,993` | `-sT -sV --version-light --script imap-capabilities --script-timeout 30s --host-timeout 5m --open` |
| `scan_imap_ntlm_info.py` | Mail: IMAP NTLM metadata | low | authorized | no | `143,993` | `-sT -sV --version-light --script imap-ntlm-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_pop3_capabilities.py` | Mail: POP3 capabilities | low | authorized | no | `110,995` | `-sT -sV --version-light --script pop3-capabilities --script-timeout 30s --host-timeout 5m --open` |
| `scan_pop3_ntlm_info.py` | Mail: POP3 NTLM metadata | low | authorized | no | `110,995` | `-sT -sV --version-light --script pop3-ntlm-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_smtp_commands.py` | Mail: SMTP commands | low | authorized | no | `25,465,587` | `-sT -sV --version-light --script smtp-commands --script-timeout 30s --host-timeout 5m --open` |
| `scan_smtp_ntlm_info.py` | Mail: SMTP NTLM metadata | low | authorized | no | `25,465,587` | `-sT -sV --version-light --script smtp-ntlm-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_smtp_open_relay.py` | Mail: relay configuration | medium | authorized | no | `25,465,587` | `-sT -sV --version-light --script smtp-open-relay --script-timeout 30s --host-timeout 5m --open` |
| `scan_smtp_strangeport.py` | Mail: SMTP on unusual ports | low | authorized | no | `25,465,587,2525` | `-sT -sV --version-light --script smtp-strangeport --script-timeout 30s --host-timeout 5m --open` |

## nse (15)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_address_info.py` | Address metadata | low | authorized | no | `22,80,443` | `-sT -sV --version-light --script address-info --script-timeout 30s --open` |
| `scan_clock_skew.py` | Clock-skew inspection | low | authorized | no | `22,25,80,123,443` | `-sT -sV --version-light --script clock-skew --script-timeout 30s --open` |
| `scan_duplicate_addresses.py` | Duplicate address check | low | authorized | no | `22,80,443` | `-sT -sV --version-light --script duplicates --script-timeout 30s --open` |
| `scan_fingerprint_strings.py` | Unknown service strings | low | authorized | no | `21,22,23,25,80,443,8000,9000` | `-sT -sV --version-light --script fingerprint-strings --script-timeout 30s --open` |
| `scan_forward_reverse_dns.py` | Forward-confirmed reverse DNS | low | authorized | no | `53` | `-sT -sV --version-light --script fcrdns --script-timeout 30s --open` |
| `scan_nse_default_profile.py` | Default NSE suite | medium | authorized | no | `22,80,443,8000,9000` | `-sT -sV --version-light --script default --script-timeout 30s --open` |
| `scan_nse_discovery_profile.py` | Discovery NSE suite | medium | private | no | `22,53,80,443,8000` | `-sT -sV --version-light --script discovery --script-timeout 30s --open` |
| `scan_nse_intrusive_loopback.py` | Intrusive NSE loopback | high | loopback | no | `2222,8000,9000` | `-sT -sV --script intrusive --script-timeout 60s --open` |
| `scan_nse_safe_profile.py` | Safe NSE suite | low | authorized | no | `22,80,443,8000,9000` | `-sT -sV --version-light --script default and safe --script-timeout 30s --open` |
| `scan_nse_version_profile.py` | Version NSE suite | medium | authorized | no | `22,80,443,8000,9000` | `-sT -sV --version-light --script version --script-timeout 30s --open` |
| `scan_nse_vuln_loopback.py` | Vulnerability NSE loopback | high | loopback | no | `2222,8000,9000` | `-sT -sV --script vuln --script-timeout 60s --open` |
| `scan_path_mtu.py` | Path MTU discovery | low | authorized | no | `22,80,443` | `-sT -sV --version-light --script path-mtu --script-timeout 30s --open` |
| `scan_scripts_default.py` | Default NSE | medium | authorized | no | — | `-sT -sV --script default --top-ports 100` |
| `scan_scripts_default_safe.py` | Default and safe NSE | low | authorized | no | — | `-sT -sV --script default and safe --top-ports 100` |
| `scan_scripts_safe.py` | Safe NSE | medium | authorized | no | — | `-sT -sV --script safe --top-ports 100` |

## remote (18)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_ftp_anonymous.py` | FTP anonymous access | medium | private | no | `21` | `-sT -sV --version-light --script ftp-anon --script-timeout 30s --open` |
| `scan_ftp_system.py` | FTP system type | low | authorized | no | `21` | `-sT -sV --version-light --script ftp-syst --script-timeout 30s --open` |
| `scan_nfs_exports.py` | NFS exports | medium | private | no | `111,2049` | `-sT -sV --version-light --script nfs-showmount --script-timeout 30s --open` |
| `scan_nfs_listing.py` | NFS directory listing | medium | private | no | `111,2049` | `-sT -sV --version-light --script nfs-ls --script-timeout 30s --open` |
| `scan_nfs_stats.py` | NFS filesystem stats | medium | private | no | `111,2049` | `-sT -sV --version-light --script nfs-statfs --script-timeout 30s --open` |
| `scan_rdp_encryption.py` | RDP encryption | low | authorized | no | `3389` | `-sT -sV --version-light --script rdp-enum-encryption --script-timeout 30s --open` |
| `scan_rdp_ntlm.py` | RDP NTLM metadata | low | authorized | no | `3389` | `-sT -sV --version-light --script rdp-ntlm-info --script-timeout 30s --open` |
| `scan_rpcinfo.py` | RPC program listing | low | authorized | no | `111` | `-sT -sV --version-light --script rpcinfo --script-timeout 30s --open` |
| `scan_smb2_capabilities.py` | SMB2 capabilities | low | authorized | no | `445` | `-sT -sV --version-light --script smb2-capabilities --script-timeout 30s --open` |
| `scan_smb2_security_mode.py` | SMB2 security mode | low | authorized | no | `445` | `-sT -sV --version-light --script smb2-security-mode --script-timeout 30s --open` |
| `scan_smb2_time.py` | SMB2 server time | low | authorized | no | `445` | `-sT -sV --version-light --script smb2-time --script-timeout 30s --open` |
| `scan_smb_os.py` | SMB OS discovery | low | authorized | no | `139,445` | `-sT -sV --version-light --script smb-os-discovery --script-timeout 30s --open` |
| `scan_smb_shares.py` | SMB shares | medium | private | no | `139,445` | `-sT -sV --version-light --script smb-enum-shares --script-timeout 30s --open` |
| `scan_smb_users.py` | SMB users | medium | private | no | `139,445` | `-sT -sV --version-light --script smb-enum-users --script-timeout 30s --open` |
| `scan_smtp_ntlm.py` | SMTP NTLM metadata | low | authorized | no | `25,465,587` | `-sT -sV --version-light --script smtp-ntlm-info --script-timeout 30s --open` |
| `scan_ssh_algorithms.py` | SSH algorithms | low | authorized | no | `22,2222` | `-sT -sV --version-light --script ssh2-enum-algos --script-timeout 30s --open` |
| `scan_ssh_host_keys.py` | SSH host keys | low | authorized | no | `22,2222` | `-sT -sV --version-light --script ssh-hostkey --script-timeout 30s --open` |
| `scan_ssh_version1.py` | SSH version 1 support | low | authorized | no | `22,2222` | `-sT -sV --version-light --script sshv1 --script-timeout 30s --open` |

## service (23)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_aggressive_loopback.py` | Aggressive loopback profile | high | loopback | yes | `2222,8000,9000` | `-A --reason` |
| `scan_banner_grab.py` | Generic banner collection | low | authorized | no | `21,22,23,25,80,110,143,443,8000,9000` | `-sT -sV --version-light --script banner --script-timeout 30s --open` |
| `scan_os_fingerprint.py` | OS fingerprint | medium | authorized | yes | — | `-O --osscan-limit --max-os-tries 1 --top-ports 1000` |
| `scan_os_guess.py` | Aggressive OS guess | medium | authorized | yes | — | `-O --osscan-guess --max-os-tries 1 --top-ports 1000` |
| `scan_os_guess_profile.py` | Aggressive OS guessing | medium | authorized | yes | — | `-O --osscan-guess --top-ports 1000 --reason` |
| `scan_os_limited_profile.py` | Limited OS fingerprint | medium | authorized | yes | — | `-O --osscan-limit --max-os-tries 1 --top-ports 1000 --reason` |
| `scan_os_service_combo.py` | OS and service inventory | medium | authorized | yes | — | `-O -sV --version-light --top-ports 1000 --reason --open` |
| `scan_os_standard_profile.py` | Standard OS fingerprint | medium | authorized | yes | — | `-O --top-ports 1000 --reason` |
| `scan_rpc.py` | RPC service scan | medium | authorized | no | `111,135,593,2049` | `-sT -sV -sR` |
| `scan_rpc_services.py` | RPC service scan | medium | authorized | no | `111,2049,32768-32775` | `-sT -sR --reason --open` |
| `scan_service_all.py` | Full service detection | medium | authorized | no | — | `-sT -sV --version-all --top-ports 100` |
| `scan_service_banner.py` | Generic banners | low | authorized | no | `21,22,25,80,110,143,443,8000,9000` | `-sT -sV --script banner` |
| `scan_service_default.py` | Default service detection | low | authorized | no | — | `-sT -sV --top-ports 100` |
| `scan_service_light.py` | Light service detection | low | authorized | no | — | `-sT -sV --version-light --top-ports 100` |
| `scan_version_all_profile.py` | Full version detection | medium | authorized | no | `22,80,443,8000,9000` | `-sT -sV --version-all --reason --open` |
| `scan_version_allports_lab.py` | Version all-ports override | medium | loopback | no | `2222,8000,9000` | `-sT -sV --allports --version-light --reason --open` |
| `scan_version_intensity_default.py` | Version intensity 5 | low | authorized | no | `22,80,443,8000,9000` | `-sT -sV --version-intensity 5 --reason --open` |
| `scan_version_intensity_nine.py` | Version intensity 9 | low | authorized | no | `22,80,443,8000,9000` | `-sT -sV --version-intensity 9 --reason --open` |
| `scan_version_intensity_seven.py` | Version intensity 7 | low | authorized | no | `22,80,443,8000,9000` | `-sT -sV --version-intensity 7 --reason --open` |
| `scan_version_intensity_two.py` | Version intensity 2 | low | authorized | no | `22,80,443,8000,9000` | `-sT -sV --version-intensity 2 --reason --open` |
| `scan_version_intensity_zero.py` | Version intensity 0 | low | authorized | no | `22,80,443,8000,9000` | `-sT -sV --version-intensity 0 --reason --open` |
| `scan_version_light_profile.py` | Light version detection | low | authorized | no | `22,80,443,8000,9000` | `-sT -sV --version-light --reason --open` |
| `scan_version_trace_lab.py` | Version probe trace | high | loopback | no | `2222,8000,9000` | `-sT -sV --version-trace --reason --open` |

## smb (11)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_smb_enum_domains.py` | SMB: domains | medium | authorized | no | `139,445` | `-sT -sV --version-light --script smb-enum-domains --script-timeout 30s --host-timeout 5m --open` |
| `scan_smb_enum_groups.py` | SMB: groups | medium | authorized | no | `139,445` | `-sT -sV --version-light --script smb-enum-groups --script-timeout 30s --host-timeout 5m --open` |
| `scan_smb_enum_services.py` | SMB: services | medium | authorized | no | `139,445` | `-sT -sV --version-light --script smb-enum-services --script-timeout 30s --host-timeout 5m --open` |
| `scan_smb_enum_sessions.py` | SMB: sessions | medium | authorized | no | `139,445` | `-sT -sV --version-light --script smb-enum-sessions --script-timeout 30s --host-timeout 5m --open` |
| `scan_smb_enum_shares.py` | SMB: shares | medium | authorized | no | `139,445` | `-sT -sV --version-light --script smb-enum-shares --script-timeout 30s --host-timeout 5m --open` |
| `scan_smb_enum_users.py` | SMB: users | medium | authorized | no | `139,445` | `-sT -sV --version-light --script smb-enum-users --script-timeout 30s --host-timeout 5m --open` |
| `scan_smb_os_discovery.py` | SMB: OS metadata | low | authorized | no | `139,445` | `-sT -sV --version-light --script smb-os-discovery --script-timeout 30s --host-timeout 5m --open` |
| `scan_smb_protocols.py` | SMB: protocol dialects | low | authorized | no | `139,445` | `-sT -sV --version-light --script smb-protocols --script-timeout 30s --host-timeout 5m --open` |
| `scan_smb_security_mode.py` | SMB: signing and authentication mode | low | authorized | no | `139,445` | `-sT -sV --version-light --script smb-security-mode --script-timeout 30s --host-timeout 5m --open` |
| `scan_smb_server_stats.py` | SMB: server statistics | medium | authorized | no | `139,445` | `-sT -sV --version-light --script smb-server-stats --script-timeout 30s --host-timeout 5m --open` |
| `scan_smb_system_info.py` | SMB: system information | medium | authorized | no | `139,445` | `-sT -sV --version-light --script smb-system-info --script-timeout 30s --host-timeout 5m --open` |

## snmp (7)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_snmp_info.py` | SNMP: system information | low | authorized | yes | `161` | `-sU -sV --version-light --script snmp-info --script-timeout 30s --host-timeout 5m --open` |
| `scan_snmp_interfaces.py` | SNMP: interfaces | medium | authorized | yes | `161` | `-sU -sV --version-light --script snmp-interfaces --script-timeout 30s --host-timeout 5m --open` |
| `scan_snmp_netstat.py` | SNMP: network tables | medium | authorized | yes | `161` | `-sU -sV --version-light --script snmp-netstat --script-timeout 30s --host-timeout 5m --open` |
| `scan_snmp_processes.py` | SNMP: processes | medium | authorized | yes | `161` | `-sU -sV --version-light --script snmp-processes --script-timeout 30s --host-timeout 5m --open` |
| `scan_snmp_sysdescr.py` | SNMP: system description | low | authorized | yes | `161` | `-sU -sV --version-light --script snmp-sysdescr --script-timeout 30s --host-timeout 5m --open` |
| `scan_snmp_win32_services.py` | SNMP: Windows services | medium | authorized | yes | `161` | `-sU -sV --version-light --script snmp-win32-services --script-timeout 30s --host-timeout 5m --open` |
| `scan_snmp_win32_software.py` | SNMP: Windows software | medium | authorized | yes | `161` | `-sU -sV --version-light --script snmp-win32-software --script-timeout 30s --host-timeout 5m --open` |

## ssh (4)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_ssh2_enum_algos.py` | SSH: protocol algorithms | low | authorized | no | `22,2222` | `-sT -sV --version-light --script ssh2-enum-algos --script-timeout 30s --host-timeout 5m --open` |
| `scan_ssh_auth_methods.py` | SSH: authentication methods | medium | authorized | no | `22,2222` | `-sT -sV --version-light --script ssh-auth-methods --script-timeout 30s --host-timeout 5m --open` |
| `scan_ssh_hostkey.py` | SSH: host-key fingerprints | low | authorized | no | `22,2222` | `-sT -sV --version-light --script ssh-hostkey --script-timeout 30s --host-timeout 5m --open` |
| `scan_sshv1.py` | SSH: obsolete protocol v1 support | low | authorized | no | `22,2222` | `-sT -sV --version-light --script sshv1 --script-timeout 30s --host-timeout 5m --open` |

## tcp (27)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_tcp_ack_all.py` | Full TCP ACK firewall map | high | loopback | yes | — | `-sA -p- --reason` |
| `scan_tcp_ack_common.py` | TCP ACK firewall map | medium | authorized | yes | — | `-sA --top-ports 100 --reason` |
| `scan_tcp_connect_all.py` | Full TCP connect scan | medium | authorized | no | — | `-sT -p- --reason --open` |
| `scan_tcp_connect_fast.py` | TCP connect fast list | low | authorized | no | — | `-sT -F --reason --open` |
| `scan_tcp_connect_top10.py` | TCP connect top 10 | low | authorized | no | — | `-sT --top-ports 10 --reason --open` |
| `scan_tcp_connect_top100.py` | TCP connect top 100 | low | authorized | no | — | `-sT --top-ports 100 --reason --open` |
| `scan_tcp_connect_top1000.py` | TCP connect top 1000 | low | authorized | no | — | `-sT --top-ports 1000 --reason --open` |
| `scan_tcp_custom_ackrst_lab.py` | Custom ACK/RST flags | high | loopback | yes | — | `-sA --scanflags ACKRST --top-ports 100 --reason` |
| `scan_tcp_custom_synfin_lab.py` | Custom SYN/FIN flags | high | loopback | yes | — | `-sS --scanflags SYNFIN --top-ports 100 --reason` |
| `scan_tcp_data_length_lab.py` | Extra payload TCP lab | high | loopback | yes | — | `-sS --data-length 16 --top-ports 100 --reason` |
| `scan_tcp_defeat_rst_rate_limit.py` | RST rate-limit comparison | medium | private | yes | — | `-sS --top-ports 1000 --defeat-rst-ratelimit --reason --open` |
| `scan_tcp_fin_common.py` | TCP FIN scan | medium | authorized | yes | — | `-sF --top-ports 100 --reason` |
| `scan_tcp_fragment_lab.py` | Fragmented SYN lab | high | loopback | yes | — | `-sS -f --top-ports 100 --reason` |
| `scan_tcp_host_timeout.py` | Bounded TCP scan | low | authorized | no | — | `-sT --top-ports 1000 --host-timeout 30s --reason --open` |
| `scan_tcp_low_retries.py` | Low-retry TCP scan | medium | private | no | — | `-sT --top-ports 100 --max-retries 1 --reason --open` |
| `scan_tcp_maimon_common.py` | TCP Maimon scan | medium | authorized | yes | — | `-sM --top-ports 100 --reason` |
| `scan_tcp_mtu24_lab.py` | Custom MTU SYN lab | high | loopback | yes | — | `-sS --mtu 24 --top-ports 100 --reason` |
| `scan_tcp_null_common.py` | TCP null scan | medium | authorized | yes | — | `-sN --top-ports 100 --reason` |
| `scan_tcp_open_only_1000.py` | Open-only TCP top 1000 | low | authorized | no | — | `-sT --top-ports 1000 --reason --open` |
| `scan_tcp_packet_trace_lab.py` | TCP packet trace | high | loopback | no | `8000` | `-sT --packet-trace --reason` |
| `scan_tcp_syn_all.py` | Full TCP SYN scan | medium | authorized | yes | — | `-sS -p- --reason --open` |
| `scan_tcp_syn_top10.py` | TCP SYN top 10 | medium | authorized | yes | — | `-sS --top-ports 10 --reason --open` |
| `scan_tcp_syn_top100.py` | TCP SYN top 100 | medium | authorized | yes | — | `-sS --top-ports 100 --reason --open` |
| `scan_tcp_syn_top1000.py` | TCP SYN top 1000 | medium | authorized | yes | — | `-sS --top-ports 1000 --reason --open` |
| `scan_tcp_window_common.py` | TCP window scan | medium | authorized | yes | — | `-sW --top-ports 100 --reason` |
| `scan_tcp_without_discovery.py` | TCP scan without discovery | low | authorized | no | — | `-Pn -sT --top-ports 100 --reason --open` |
| `scan_tcp_xmas_common.py` | TCP Xmas scan | medium | authorized | yes | — | `-sX --top-ports 100 --reason` |

## tls (14)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_ssl_cert.py` | TLS: certificate details | low | authorized | no | `443,465,636,853,993,995,8443` | `-sT -sV --version-light --script ssl-cert --script-timeout 30s --host-timeout 5m --open` |
| `scan_ssl_cert_intaddr.py` | TLS: internal certificate addresses | low | authorized | no | `443,465,636,853,993,995,8443` | `-sT -sV --version-light --script ssl-cert-intaddr --script-timeout 30s --host-timeout 5m --open` |
| `scan_ssl_date.py` | TLS: service clock | low | authorized | no | `443,465,636,853,993,995,8443` | `-sT -sV --version-light --script ssl-date --script-timeout 30s --host-timeout 5m --open` |
| `scan_ssl_dh_params.py` | TLS: DH parameters | medium | authorized | no | `443,465,636,853,993,995,8443` | `-sT -sV --version-light --script ssl-dh-params --script-timeout 30s --host-timeout 5m --open` |
| `scan_ssl_enum_ciphers.py` | TLS: versions and ciphers | medium | authorized | no | `443,465,636,853,993,995,8443` | `-sT -sV --version-light --script ssl-enum-ciphers --script-timeout 30s --host-timeout 5m --open` |
| `scan_ssl_known_key.py` | TLS: known-key matches | low | authorized | no | `443,465,636,853,993,995,8443` | `-sT -sV --version-light --script ssl-known-key --script-timeout 30s --host-timeout 5m --open` |
| `scan_tls_alpn.py` | TLS: ALPN protocols | low | authorized | no | `443,465,636,853,993,995,8443` | `-sT -sV --version-light --script tls-alpn --script-timeout 30s --host-timeout 5m --open` |
| `scan_tls_ccs_loopback.py` | TLS CCS injection check | high | loopback | no | `443,8443` | `-sT -sV --version-light --script ssl-ccs-injection --script-timeout 30s --open` |
| `scan_tls_certificate.py` | TLS certificate | low | authorized | no | `443,465,636,853,993,995,8443` | `-sT -sV --version-light --script ssl-cert --script-timeout 30s --open` |
| `scan_tls_ciphers.py` | TLS cipher suites | medium | authorized | no | `443,465,636,853,993,995,8443` | `-sT -sV --version-light --script ssl-enum-ciphers --script-timeout 30s --open` |
| `scan_tls_date.py` | TLS server date | low | authorized | no | `443,465,636,853,993,995,8443` | `-sT -sV --version-light --script ssl-date --script-timeout 30s --open` |
| `scan_tls_dh_params.py` | TLS Diffie-Hellman parameters | medium | authorized | no | `443,465,636,853,993,995,8443` | `-sT -sV --version-light --script ssl-dh-params --script-timeout 30s --open` |
| `scan_tls_heartbleed_loopback.py` | TLS Heartbleed check | high | loopback | no | `443,8443` | `-sT -sV --version-light --script ssl-heartbleed --script-timeout 30s --open` |
| `scan_tls_nextprotoneg.py` | TLS: legacy next protocols | low | authorized | no | `443,465,636,853,993,995,8443` | `-sT -sV --version-light --script tls-nextprotoneg --script-timeout 30s --host-timeout 5m --open` |

## transport (47)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_ip_protocols.py` | IP protocols | medium | authorized | yes | — | `-sO` |
| `scan_mixed_tcp_udp.py` | Mixed TCP and UDP | medium | authorized | yes | — | `-sT -sU -p T:22,80,443,U:53,123,161` |
| `scan_mixed_tcp_udp_common.py` | Mixed TCP and UDP | medium | authorized | yes | `T:22,80,443,8000,U:53,123,161,5353` | `-sS -sU --reason --open` |
| `scan_sctp_cookie.py` | SCTP COOKIE | medium | authorized | yes | `80,2905,3868` | `-sZ` |
| `scan_sctp_cookie_common.py` | SCTP COOKIE-ECHO scan | medium | authorized | yes | `80,443,3868,9899` | `-sZ --reason` |
| `scan_sctp_init.py` | SCTP INIT | medium | authorized | yes | `80,2905,3868` | `-sY` |
| `scan_sctp_init_common.py` | SCTP INIT scan | medium | authorized | yes | `80,443,3868,9899` | `-sY --reason --open` |
| `scan_sctp_version_common.py` | SCTP service detection | medium | authorized | yes | `80,443,3868,9899` | `-sY -sV --version-light --reason --open` |
| `scan_tcp_admin_ports.py` | Administration ports | low | authorized | no | `22,23,161,443,445,3389,5900,5985,5986` | `-sT` |
| `scan_tcp_common.py` | Common services | low | authorized | no | `21,22,23,25,53,80,110,139,143,443,445,587,993,995,3389` | `-sT` |
| `scan_tcp_connect.py` | TCP connect | low | authorized | no | `22,80,443,8000` | `-sT` |
| `scan_tcp_database_ports.py` | Database ports | low | authorized | no | `523,1433,1521,27017,3306,5432,5984,6379,9042,11211` | `-sT` |
| `scan_tcp_devops_ports.py` | DevOps ports | low | authorized | no | `2375,2376,6443,8001,8080,8443,9090,10250` | `-sT` |
| `scan_tcp_fast.py` | Fast TCP | low | authorized | no | — | `-sT -F` |
| `scan_tcp_file_ports.py` | File-service ports | low | authorized | no | `20,21,22,111,139,445,873,2049` | `-sT` |
| `scan_tcp_fin.py` | TCP FIN | medium | authorized | yes | `22,80,443` | `-sF` |
| `scan_tcp_full.py` | Full TCP | medium | authorized | no | — | `-sT -p-` |
| `scan_tcp_mail_ports.py` | Mail ports | low | authorized | no | `25,110,143,465,587,993,995` | `-sT` |
| `scan_tcp_maimon.py` | TCP Maimon | medium | authorized | yes | `22,80,443` | `-sM` |
| `scan_tcp_no_ping.py` | Known-up TCP | medium | authorized | no | — | `-sT -Pn --top-ports 100` |
| `scan_tcp_null.py` | TCP NULL | medium | authorized | yes | `22,80,443` | `-sN` |
| `scan_tcp_remote_desktop_ports.py` | Remote-display ports | low | authorized | no | `3389,5800,5900-5903,6000-6003` | `-sT` |
| `scan_tcp_sequential.py` | Sequential TCP | low | authorized | no | `20-25,53,80,110,139,143,443,445` | `-sT -r` |
| `scan_tcp_syn.py` | TCP SYN | medium | authorized | yes | `22,80,443,8000` | `-sS` |
| `scan_tcp_top_10.py` | Top 10 TCP | low | authorized | no | — | `-sT --top-ports 10` |
| `scan_tcp_top_100.py` | Top 100 TCP | low | authorized | no | — | `-sT --top-ports 100` |
| `scan_tcp_top_1000.py` | Top 1000 TCP | medium | authorized | no | — | `-sT --top-ports 1000` |
| `scan_tcp_web_ports.py` | Web ports | low | authorized | no | `80,443,3000,5000,8000,8008,8080,8081,8443,8888` | `-sT` |
| `scan_tcp_xmas.py` | TCP Xmas | medium | authorized | yes | `22,80,443` | `-sX` |
| `scan_udp_all_lab.py` | Full UDP loopback scan | high | loopback | yes | — | `-sU -p- --reason --open` |
| `scan_udp_common.py` | Common UDP | medium | authorized | yes | `53,123,161,500,5353` | `-sU` |
| `scan_udp_dhcp.py` | UDP DHCP ports | medium | private | yes | `67,68` | `-sU --reason --open` |
| `scan_udp_dns.py` | UDP DNS ports | medium | authorized | yes | `53,5353` | `-sU --reason --open` |
| `scan_udp_ntp.py` | UDP NTP | medium | authorized | yes | `123` | `-sU --reason --open` |
| `scan_udp_packet_trace_lab.py` | UDP packet trace | high | loopback | yes | `5353` | `-sU --packet-trace --reason` |
| `scan_udp_radius.py` | UDP RADIUS | medium | authorized | yes | `1812,1813` | `-sU --reason --open` |
| `scan_udp_rip.py` | UDP routing protocols | medium | private | yes | `520,521` | `-sU --reason --open` |
| `scan_udp_service_discovery.py` | UDP discovery services | medium | private | yes | `1900,3702,5353` | `-sU --reason --open` |
| `scan_udp_snmp.py` | UDP SNMP | medium | authorized | yes | `161,162` | `-sU --reason --open` |
| `scan_udp_syslog.py` | UDP syslog | medium | authorized | yes | `514` | `-sU --reason --open` |
| `scan_udp_tftp.py` | UDP TFTP | medium | authorized | yes | `69` | `-sU --reason --open` |
| `scan_udp_top100_profile.py` | UDP top 100 | medium | authorized | yes | — | `-sU --top-ports 100 --reason --open` |
| `scan_udp_top10_profile.py` | UDP top 10 | medium | authorized | yes | — | `-sU --top-ports 10 --reason --open` |
| `scan_udp_top_100.py` | Top 100 UDP | medium | authorized | yes | — | `-sU --top-ports 100` |
| `scan_udp_top_20.py` | Top 20 UDP | medium | authorized | yes | — | `-sU --top-ports 20` |
| `scan_udp_version_common.py` | UDP service detection | medium | authorized | yes | `53,69,123,161,500,5353` | `-sU -sV --version-light --reason --open` |
| `scan_udp_vpn.py` | UDP VPN ports | medium | authorized | yes | `500,1701,4500` | `-sU --reason --open` |

## web (13)

| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |
|---|---|---|---|---|---|---|
| `scan_http_apache_status.py` | Apache status page | medium | private | no | `80,443,8000,8080,8443` | `-sT -sV --version-light --script http-apache-server-status --script-timeout 30s --open` |
| `scan_http_bigip_cookie.py` | BIG-IP cookie metadata | low | authorized | no | `80,443,8000,8080,8443` | `-sT -sV --version-light --script http-bigip-cookie --script-timeout 30s --open` |
| `scan_http_comments.py` | HTTP comments | medium | private | no | `80,443,8000,8080,8443` | `-sT -sV --version-light --script http-comments-displayer --script-timeout 30s --open` |
| `scan_http_cross_domain.py` | Cross-domain policy | low | authorized | no | `80,443,8000,8080,8443` | `-sT -sV --version-light --script http-cross-domain-policy --script-timeout 30s --open` |
| `scan_http_drupal_loopback.py` | Drupal enumeration | high | loopback | no | `8000` | `-sT -sV --version-light --script http-drupal-enum --script-timeout 30s --open` |
| `scan_http_enum_loopback.py` | HTTP path enumeration | high | loopback | no | `8000` | `-sT -sV --version-light --script http-enum --script-timeout 30s --open` |
| `scan_http_errors.py` | HTTP error pages | medium | private | no | `80,443,8000,8080,8443` | `-sT -sV --version-light --script http-errors --script-timeout 30s --open` |
| `scan_http_internal_ip.py` | HTTP internal IP disclosure | medium | private | no | `80,443,8000,8080,8443` | `-sT -sV --version-light --script http-internal-ip-disclosure --script-timeout 30s --open` |
| `scan_http_jsonp.py` | JSONP endpoint detection | medium | private | no | `80,443,8000,8080,8443` | `-sT -sV --version-light --script http-jsonp-detection --script-timeout 30s --open` |
| `scan_http_robots.py` | HTTP robots file | low | authorized | no | `80,443,8000,8080,8443` | `-sT -sV --version-light --script http-robots.txt --script-timeout 30s --open` |
| `scan_http_waf.py` | Web application firewall detection | medium | private | no | `80,443,8000,8080,8443` | `-sT -sV --version-light --script http-waf-detect --script-timeout 30s --open` |
| `scan_http_webdav.py` | WebDAV inspection | medium | private | no | `80,443,8000,8080,8443` | `-sT -sV --version-light --script http-webdav-scan --script-timeout 30s --open` |
| `scan_http_wordpress_loopback.py` | WordPress enumeration | high | loopback | no | `8000` | `-sT -sV --version-light --script http-wordpress-enum --script-timeout 30s --open` |
