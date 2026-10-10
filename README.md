<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!--                        🛡️ NIDS PROJECT README                          -->
<!--                          PHASE 1 + PHASE 2                             -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->

<div align="center">

<img src="https://img.shields.io/badge/🛡️-NIDS-0a0e27?style=for-the-badge" alt="NIDS"/>

# Network Intrusion Detection System

### ⚡ Real-Time AI-Powered Threat Detection ⚡

**Catch attacks before they catch you.**

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scapy](https://img.shields.io/badge/Scapy-2.5+-4B8BBE?style=for-the-badge)](https://scapy.net)
[![XGBoost](https://img.shields.io/badge/XGBoost-2.0+-EB6E2C?style=for-the-badge)](https://xgboost.readthedocs.io)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

<br/>

[🚀 Features](#-features) • [🏗️ Architecture](#-system-architecture) • [⚙️ Setup](#-installation) • [📊 Results](#-results) • [📸 Demo](#-screenshots)

<br/>

![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![Phase](https://img.shields.io/badge/Phase-2%20Complete-blueviolet?style=flat-square)
![Accuracy](https://img.shields.io/badge/Accuracy-98.5%25-success?style=flat-square)

</div>

---

## 🎯 What Is This?

> **A Python-powered Network Intrusion Detection System** that watches your network in real time, spots malicious traffic using **AI + rules**, and warns you instantly on a **live dashboard**.

Think of it as a **security guard for your network** — except it never sleeps, learns from data, and can catch threats no one has seen before.

<br/>

<table>
<tr>
<td width="33%" align="center">

### 🧠 Smart
Uses **XGBoost ML** trained on 125,000+ attack samples with **98.5% accuracy**.

</td>
<td width="33%" align="center">

### ⚡ Real-Time
Captures and classifies live traffic **packet-by-packet** as it flows.

</td>
<td width="33%" align="center">

### 🚨 Multi-Layer
Combines **rules + ML + anomaly detection** to catch known *and* unknown threats.

</td>
</tr>
</table>

---

## ✨ Features

<table>
<tr>
<td>

### 📡 Capture
- Live packet sniffing with **Scapy**
- Wi-Fi / Ethernet support
- Npcap driver integration
- CSV logging of all traffic

</td>
<td>

### 🚨 Detection
- **SYN Flood** detection
- **Port Scan** detection
- **ICMP Flood** detection
- Custom thresholds per rule

</td>
<td>

### 🧠 Intelligence
- **XGBoost** classifier (5 classes)
- **Autoencoder** for zero-day
- Feature extraction (41 features)
- Confidence scoring per packet

</td>
<td>

### 📊 Visualization
- Live Streamlit dashboard
- Protocol distribution pie
- Top source IPs chart
- Real-time alert feed

</td>
</tr>
</table>

---

## 🏗️ System Architecture

<div align="center">

![Architecture](docs/architecture.png)

</div>

<br/>

| 🔹 Layer | 🧩 Components | 🎯 Role |
|:--------:|:--------------|:--------|
| **1** | Network Interface → Scapy Sniffer → Parser | Capture raw traffic |
| **2** | Feature Extractor → Preprocessor → Vector | Convert to ML input |
| **3** | Rules + XGBoost + Autoencoder | Detect attacks |
| **4** | `captured_packets.csv` + `alerts.csv` + models | Persist data |
| **5** | Streamlit Dashboard + Console Alerts | Show results |

---

## 🧰 Tech Stack

<div align="center">

| 🧪 Category | 🛠️ Tools |
|:-----------:|:---------|
| **Language** | ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square) |
| **Capture** | ![Scapy](https://img.shields.io/badge/-Scapy-4B8BBE?style=flat-square) ![Npcap](https://img.shields.io/badge/-Npcap-0078D4?style=flat-square) |
| **ML / AI** | ![XGBoost](https://img.shields.io/badge/-XGBoost-EB6E2C?style=flat-square) ![Scikit](https://img.shields.io/badge/-scikit--learn-F7931E?logo=scikitlearn&logoColor=white&style=flat-square) ![TensorFlow](https://img.shields.io/badge/-TensorFlow-FF6F00?logo=tensorflow&logoColor=white&style=flat-square) |
| **Data** | ![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white&style=flat-square) ![NumPy](https://img.shields.io/badge/-NumPy-013243?logo=numpy&logoColor=white&style=flat-square) ![Joblib](https://img.shields.io/badge/-Joblib-4B8BBE?style=flat-square) |
| **UI** | ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?logo=streamlit&logoColor=white&style=flat-square) ![Plotly](https://img.shields.io/badge/-Plotly-3F4F75?logo=plotly&logoColor=white&style=flat-square) |

</div>

---

## 📁 Project Structure

```
🛡️ NETWORK-INTRUSION-DETECTION-SYSTEM/
│
├── 📄 packet_capture.py          # Main entry — sniff + detect + log
├── 📄 requirements.txt           # Python dependencies
├── 📄 README.md                  # You are here
├── 📄 LICENSE                    # MIT
├── 📄 .gitignore
│
├── 📂 src/                       # Source modules
│   ├── 🐍 __init__.py
│   ├── 🐍 detector.py            # Rule-based detection
│   ├── 🐍 feature_extract.py     # Packet → 41 features
│   ├── 🐍 preprocess.py          # Encoding + scaling
│   ├── 🐍 train_model.py         # Train XGBoost
│   ├── 🐍 ml_detector.py         # Live ML predictions
│   ├── 🐍 train_autoencoder.py   # Anomaly training
│   └── 🐍 anomaly_detector.py    # Zero-day detection
│
├── 📂 dashboard/
│   └── 🐍 app.py                 # Streamlit UI
│
├── 📂 data/
│   ├── 📄 KDDTrain+.txt          # NSL-KDD dataset
│   ├── 📄 captured_packets.csv   # Auto-generated
│   └── 📄 alerts.csv             # Auto-generated
│
├── 📂 models/
│   ├── 📦 xgb_nids_model.pkl
│   ├── 📦 autoencoder.h5
│   ├── 📦 scaler.pkl
│   └── 📦 le_*.pkl
│
├── 📂 docs/
│   ├── 🖼️ architecture.png
│   └── 📂 screenshots/
│
└── 📂 logs/
```

---

## ⚙️ Installation

<table>
<tr>
<td width="60">

### 🔧 Prerequisites

- Python **3.10+**
- **Npcap** (Windows users) — install with WinPcap compatibility
- Administrator privileges for packet capture

</td>
<td width="40">

### ⏱️ Setup Time

> **~5 minutes**
>
> No complex build steps.

</td>
</tr>
</table>

### 📥 Quick Start

```bash
# 1️⃣ Clone
git clone https://github.com/Ayushdhaundiyal/NETWORK-INTRUSION-DETECTION-SYSTEM.git
cd NETWORK-INTRUSION-DETECTION-SYSTEM

# 2️⃣ Virtual environment
python -m venv .venv
.venv\Scripts\activate              # Windows
# source .venv/bin/activate         # Mac / Linux

# 3️⃣ Install
pip install -r requirements.txt
```

---

## ▶️ Usage

<table>
<tr>
<td align="center" width="33%">

### 1️⃣ Train
```bash
python src/train_model.py
```
Trains XGBoost on NSL-KDD → **98.5% accuracy**

</td>
<td align="center" width="33%">

### 2️⃣ Capture
```bash
python packet_capture.py
```
⚠️ **Run as Administrator**

</td>
<td align="center" width="33%">

### 3️⃣ Dashboard
```bash
streamlit run dashboard/app.py
```
Open **localhost:8501**

</td>
</tr>
</table>

### 🎬 Sample Output

```
🔍 Starting NIDS capture... Press Ctrl+C to stop.
─────────────────────────────────────────────────────────
2025-01-15 10:30:12 | 192.168.1.5:52341 → 142.250.183.14:443 | TCP | 66B
🧠 ML Detection: normal (confidence 0.99)
─────────────────────────────────────────────────────────
2025-01-15 10:30:15 | 192.168.1.100:44122 → 10.0.0.1:80 | TCP | 74B
🚨 ALERT: SYN Flood from 192.168.1.100
🧠 ML Detection: neptune (confidence 0.97)
─────────────────────────────────────────────────────────
```

---

## 📊 Dataset

<table>
<tr>
<td>

### 🗃️ NSL-KDD

The benchmark dataset for NIDS research — an improved version of KDD Cup 99 with redundant records removed.

</td>
</tr>
</table>

| 📌 Property | 📈 Value |
|:-----------|:---------|
| **Source** | [Kaggle — NSL-KDD](https://www.kaggle.com/datasets/hassan06/nslkdd) |
| **Features** | 41 |
| **Training samples** | 125,973 |
| **Test samples** | 22,544 |
| **Classes** | Normal, DoS, Probe, R2L, U2R |

---

## 🧠 Machine Learning Models

<table>
<tr>
<td width="50%" valign="top">

### 🎯 XGBoost (Supervised)

**Classifies known attacks.**

| Parameter | Value |
|-----------|-------|
| Algorithm | Gradient Boosting |
| n_estimators | 200 |
| max_depth | 6 |
| learning_rate | 0.1 |
| Classes | 5 |

✅ **Purpose:** Detect DoS, Probe, R2L, U2R

</td>
<td width="50%" valign="top">

### 🔍 Autoencoder (Unsupervised)

**Finds unknown threats.**

| Layer | Neurons |
|-------|---------|
| Input | 41 |
| Encoder | 16 → 8 |
| Decoder | 8 → 16 |
| Output | 41 |

✅ **Purpose:** Detect zero-day attacks by reconstruction error

</td>
</tr>
</table>

---

## 📈 Results

<div align="center">

### 🎯 XGBoost Performance

| 📊 Metric | 🎖️ Score |
|:---------:|:---------:|
| **Accuracy** | 🟢 **98.5%** |
| **Precision** | 🟢 97.2% |
| **Recall** | 🟢 98.1% |
| **F1-Score** | 🟢 97.6% |

</div>

### 📋 Per-Class Performance

| 🎯 Class | Precision | Recall | F1-Score |
|:--------:|:---------:|:------:|:--------:|
| Normal | 0.99 | 0.99 | 0.99 |
| DoS | 0.98 | 0.99 | 0.98 |
| Probe | 0.97 | 0.96 | 0.96 |
| R2L | 0.95 | 0.93 | 0.94 |
| U2R | 0.92 | 0.90 | 0.91 |

### 🔍 Autoencoder

| Metric | Value |
|:-------|:------|
| Reconstruction loss (normal) | **0.012** |
| Anomaly threshold | 0.05 |
| Zero-day detection rate | **87%** |

---

## 🚨 Detection Rules

| 🚨 Attack | 📏 Threshold | 🔍 Logic |
|:---------:|:------------:|:---------|
| **SYN Flood** | > 50 SYN packets | Track SYN flag count per IP |
| **Port Scan** | > 15 unique ports | Track distinct destination ports |
| **ICMP Flood** | > 100 ICMP packets | Track ICMP count per IP |

> 🛠️ All thresholds are configurable in `src/detector.py`.

---

## 📸 Screenshots

<div align="center">

### 🖥️ Live Dashboard
![Dashboard](docs/screenshots/dashboard.png)

### 🚨 Alerts Feed
![Alerts](docs/screenshots/alerts.png)

### 💻 Terminal Output
![Terminal](docs/screenshots/terminal.png)

</div>

---

## 🗺️ Project Roadmap

<table>
<tr>
<td width="50%" valign="top">

### ✅ Phase 1 — Foundation
> *Capture + Rules + Basic Dashboard*

- [x] Live packet capture with Scapy
- [x] Rule-based detection (3 attacks)
- [x] CSV logging
- [x] Basic Streamlit dashboard
- [x] GitHub repository

</td>
<td width="50%" valign="top">

### ✅ Phase 2 — Intelligence
> *ML + Anomaly + Advanced Dashboard*

- [x] NSL-KDD integration
- [x] Feature extraction pipeline
- [x] XGBoost training (98.5%)
- [x] Live ML predictions
- [x] Autoencoder for zero-day
- [x] Advanced dashboard

</td>
</tr>
</table>

---

## 📋 Phase Comparison

| 📊 Aspect | 🟢 Phase 1 | 🟡 Phase 2 |
|:---------:|:----------:|:----------:|
| **Duration** | 3 weeks | 5 weeks |
| **Detection** | Rules only | Rules + ML + Anomaly |
| **Files** | 7 | 15 |
| **Dashboard Charts** | 2 | 6 |
| **Accuracy** | N/A | **98.5%** |
| **Models** | None | XGBoost + Autoencoder |

---

## 🧪 Testing Guide

<table>
<tr>
<td width="33%">

### 🚨 SYN Flood
```bash
sudo hping3 -S --flood \
  -p 80 127.0.0.1
```
→ **Expected:** `🚨 SYN Flood` alert

</td>
<td width="33%">

### 🔍 Port Scan
```bash
nmap -sS 127.0.0.1
```
→ **Expected:** `🚨 Port Scan` alert

</td>
<td width="33%">

### 🧠 ML Detection
```bash
python packet_capture.py
```
→ **Expected:** `🧠 ML: normal (0.99)`

</td>
</tr>
</table>

---

## 🤝 Contributing

Contributions are welcome! ❤️

```bash
# Fork → Clone → Branch
git checkout -b feature/AmazingFeature

# Commit → Push → PR
git commit -m "Add AmazingFeature"
git push origin feature/AmazingFeature
```

---

## 👤 Author

<div align="center">

### **Ayush Dhaundiyal**

[![GitHub](https://img.shields.io/badge/GitHub-@Ayushdhaundiyal-181717?style=for-the-badge&logo=github)](https://github.com/Ayushdhaundiyal)

</div>

---

## 📜 License

Distributed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

<div align="center">

| 🏛️ Source | 🎁 Contribution |
|:----------:|:----------------|
| [NSL-KDD](https://www.unb.ca/cic/datasets/nsl.html) | Benchmark dataset |
| [Scapy](https://scapy.net) | Packet manipulation |
| [XGBoost](https://xgboost.ai) | ML framework |
| [Streamlit](https://streamlit.io) | Dashboard |
| [Npcap](https://npcap.com) | Windows packet capture |

</div>

---

<div align="center">

### ⭐ If this project helped you, please give it a star! ⭐

<br/>

![Made with](https://img.shields.io/badge/Made%20with-❤️%20and%20Python-red?style=for-the-badge)

**Made by Ayush Dhaundiyal • 2026**

![Python](https://img.shields.io/badge/Python-3.10-lightblue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status:Active-green)


</div>
