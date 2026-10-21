from src.ml_detector import ml_predict
from scapy.all import sniff, IP, TCP, UDP
from src.detector import detect
import csv
import os
from datetime import datetime

os.makedirs("data", exist_ok=True)

PACKET_FILE = "data/captured_packets.csv"
ALERT_FILE  = "data/alerts.csv"

if not os.path.exists(PACKET_FILE):
    with open(PACKET_FILE, "w", newline="") as f:
        csv.writer(f).writerow(["timestamp", "src_ip", "dst_ip", "protocol",
                                "src_port", "dst_port", "size"])

if not os.path.exists(ALERT_FILE):
    with open(ALERT_FILE, "w", newline="") as f:
        csv.writer(f).writerow(["timestamp", "alert_type", "src_ip", "details"])


def process_packet(packet):
    if IP not in packet:
        return

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    src_port = dst_port = 0
    proto_name = "OTHER"

    if TCP in packet:
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        proto_name = "TCP"
    elif UDP in packet:
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport
        proto_name = "UDP"

    size = len(packet)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(PACKET_FILE, "a", newline="") as f:
        csv.writer(f).writerow([timestamp, src_ip, dst_ip, proto_name,
                                src_port, dst_port, size])

    print(f"{timestamp} | {src_ip}:{src_port} -> {dst_ip}:{dst_port} | {proto_name} | {size}B")

    # --- RULE BASED DETECTION ---
    alerts = detect(packet)
    for alert in alerts:
        with open(ALERT_FILE, "a", newline="") as f:
            csv.writer(f).writerow([alert["timestamp"], alert["alert_type"],
                                    alert["src_ip"], alert["details"]])
        print(f" ALERT: {alert}")

    # --- MACHINE LEARNING DETECTION ---
    label, confidence = ml_predict(packet)
    print(f"    |AI says|      : {label.upper()} (Confidence: {confidence * 100:.1f}%)")


if __name__ == "__main__":
    print(" Starting NIDS capture... Press Ctrl+C to stop.")
    sniff(prn=process_packet, store=False)