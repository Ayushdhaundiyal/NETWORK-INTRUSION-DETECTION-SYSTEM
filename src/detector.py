from collections import defaultdict
from datetime import datetime
from scapy.all import IP, TCP, ICMP

syn_tracker  = defaultdict(int)
port_tracker = defaultdict(set)
icmp_tracker = defaultdict(int)

SYN_THRESHOLD       = 50
PORT_SCAN_THRESHOLD = 15
ICMP_THRESHOLD      = 100


def detect(packet):

    alerts = []

    if IP not in packet:
        return alerts

    src = packet[IP].src
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if TCP in packet and packet[TCP].flags == "S":
        syn_tracker[src] += 1
        if syn_tracker[src] > SYN_THRESHOLD:
            alerts.append({
                "timestamp": now,
                "alert_type": "SYN Flood",
                "src_ip": src,
                "details": f"{syn_tracker[src]} SYN packets"
            })

    if TCP in packet and packet[TCP].flags == "S":
        port_tracker[src].add(packet[TCP].dport)
        if len(port_tracker[src]) > PORT_SCAN_THRESHOLD:
            alerts.append({
                "timestamp": now,
                "alert_type": "Port Scan",
                "src_ip": src,
                "details": f"{len(port_tracker[src])} ports scanned"
            })

    if ICMP in packet:
        icmp_tracker[src] += 1
        if icmp_tracker[src] > ICMP_THRESHOLD:
            alerts.append({
                "timestamp": now,
                "alert_type": "ICMP Flood",
                "src_ip": src,
                "details": f"{icmp_tracker[src]} ICMP packets"
            })

    return alerts
