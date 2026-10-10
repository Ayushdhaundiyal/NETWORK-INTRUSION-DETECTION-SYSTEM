# 🛡️ Network Intrusion Detection System

A Python-based NIDS that captures live network traffic using Scapy, detects common attacks using rule-based logic, and (in later phases) uses Machine Learning for classification.

## 🚀 Features
- Live packet capture with Scapy
- Rule-based detection: SYN Flood, Port Scan, ICMP Flood
- CSV logging for packets and alerts
- Streamlit dashboard for real-time visualization

## 🧰 Tech Stack
Python, Scapy, Streamlit, Plotly, XGBoost, Scikit-learn, Joblib

## 📁 Project Structure
```
├── packet_capture.py     # main capture script
├── src/
│   └── detector.py       # rule-based detection
├── dashboard/
│   └── app.py            # Streamlit dashboard
├── data/                 # CSV logs (auto-created)
└── requirements.txt
```

## ⚙️ Installation
```bash
git clone https://github.com/Ayushdhaundiyal/NETWORK-INTRUSION-DETECTION-SYSTEM.git
cd NETWORK-INTRUSION-DETECTION-SYSTEM
pip install -r requirements.txt
```

## ▶️ Usage
Run as **Administrator**:
```bash
python packet_capture.py
```

## 📅 Project Phases
- **Phase 1** — Packet capture + rule-based detection + dashboard
- **Phase 2** — Machine Learning (XGBoost + Autoencoder)
- **Phase 3** — Deployment (Docker + alerts + tests)

## 👤 Author
**Ayush Dhaundiyal** — [@Ayushdhaundiyal](https://github.com/Ayushdhaundiyal)
