from scapy.all import sniff, IP, TCP, UDP

def process_packet(packet):

    if IP in packet:

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol = packet[IP].proto

        print("Source IP:", source_ip)
        print("Destination IP:", destination_ip)
        print("Protocol:", protocol)

        if TCP in packet:
            print("Source Port:", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)

        elif UDP in packet:
            print("Source Port:", packet[UDP].sport)
            print("Destination Port:", packet[UDP].dport)

        print("-" * 50)


sniff(prn=process_packet, count=20)