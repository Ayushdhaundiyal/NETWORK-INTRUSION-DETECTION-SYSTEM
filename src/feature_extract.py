from scapy.all import IP, TCP, UDP, ICMP

FEATURE_NAMES = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
    "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
    "num_compromised", "root_shell", "su_attempted", "num_root",
    "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds",
    "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate",
    "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate",
    "diff_srv_rate", "srv_diff_host_rate", "dst_host_count",
    "dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate", "dst_host_srv_serror_rate", "dst_host_rerror_rate",
    "dst_host_srv_rerror_rate"
]

PROTOCOL_MAP = {
    1: 0,
    6: 1,
    17: 2,
}



FLAG_MAP = {
    "S": 1,     # SYN
    "A": 0,     # ACK
    "SA": 0,    # SYN-ACK
    "F": 0,     # FIN
    "R": 2,     # RST
    "P": 0,     # PSH
    "": 0,
}


def packet_to_features(packet):

    features = {name: 0 for name in FEATURE_NAMES}

    if IP not in packet:
        return features


    features["src_bytes"] = len(packet)   # approximate
    features["dst_bytes"] = 0
    features["protocol_type"] = PROTOCOL_MAP.get(packet[IP].proto, 0)


    if TCP in packet:
        flags = str(packet[TCP].flags)
        features["flag"] = FLAG_MAP.get(flags, 0)
        features["urgent"] = packet[TCP].urgptr or 0

    elif UDP in packet:
        features["flag"] = 0


    elif ICMP in packet:
        features["flag"] = 0

    return features


def features_to_list(features_dict):

    return [features_dict[name] for name in FEATURE_NAMES]


if __name__ == "__main__":
    from scapy.all import IP, TCP


    pkt = IP(src="192.168.1.5", dst="8.8.8.8") / TCP(dport=443, flags="S")

    feats = packet_to_features(pkt)
    print("Feature dict length:", len(feats))
    print("Sample features:")
    print("  protocol_type:", feats["protocol_type"])
    print("  flag:", feats["flag"])
    print("  src_bytes:", feats["src_bytes"])

    vector = features_to_list(feats)
    print("Vector length:", len(vector))
