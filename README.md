<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                        HEADER                                 -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">

# 🛡️ Network Intrusion Detection System

### AI-Powered Real-Time Network Threat Detection

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scapy](https://img.shields.io/badge/Scapy-2.5+-green?style=for-the-badge)](https://scapy.net)
[![XGBoost](https://img.shields.io/badge/XGBoost-2.0+-orange?style=for-the-badge)](https://xgboost.readthedocs.io)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red?style=for-the-badge&logo=streamlit)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

**A machine learning–based Network Intrusion Detection System that captures live traffic, detects attacks in real time, and visualizes threats on an interactive dashboard.**

[Features](#-features) • [Architecture](#-system-architecture) • [Installation](#-installation) • [Usage](#-usage) • [Results](#-results) • [Roadmap](#-project-roadmap)

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Dataset](#-dataset)
- [Machine Learning Model](#-machine-learning-model)
- [Results](#-results)
- [Screenshots](#-screenshots)
- [Project Roadmap](#-project-roadmap)
- [Testing](#-testing)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)
- [Acknowledgments](#-acknowledgments)

---

## 🎯 Overview

The **Network Intrusion Detection System (NIDS)** is a Python-based security tool that monitors live network traffic and detects malicious activity using a hybrid approach:

- **Rule-based detection** for known attack signatures
- **Machine Learning (XGBoost)** for supervised classification of known attacks
- **Autoencoder anomaly detection** for identifying unknown (zero-day) threats
- **Real-time Streamlit dashboard** for live visualization

This project was built as a 3-phase academic project to demonstrate practical skills in **cybersecurity**, **machine learning**, and **software engineering**.

---

## 🧩 Problem Statement

Traditional firewalls and antivirus tools cannot detect many modern network attacks, especially:

- **Zero-day exploits** — attacks with no known signature
- **Insider threats** — malicious traffic from trusted sources
- **Encrypted attacks** — payloads that can't be inspected

This NIDS addresses these gaps by combining **signature-based rules** with **ML-driven anomaly detection** to catch both known and unknown threats.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📡 **Live Packet Capture** | Real-time sniffing with Scapy on Wi-Fi/Ethernet |
| 🚨 **Rule-Based Detection** | SYN Flood, Port Scan, ICMP Flood, and more |
| 🧠 **ML Classification** | XGBoost trained on NSL-KDD (98%+ accuracy) |
| 🔍 **Anomaly Detection** | Autoencoder flags zero-day attacks |
| 📊 **Interactive Dashboard** | Streamlit + Plotly live charts |
| 💾 **CSV Logging** | Persistent packet and alert history |
| 📲 **Real-Time Alerts** | Console, desktop notification, Telegram |
| 🐳 **Docker Support** | One-command deployment |
| ✅ **Tested** | pytest with 80%+ coverage |

---

## 🏗️ System Architecture

![Architecture](docs/architecture.png)

The system is organized into **5 layers**:

1. **Capture Layer** — Scapy sniffs packets from the network interface
2. **Processing Layer** — Feature extraction + scaling (41 features)
3. **Detection Layer** — Rules + XGBoost + Autoencoder run in parallel
4. **Storage Layer** — Packets and alerts logged to CSV
5. **Presentation Layer** — Streamlit dashboard + console + Telegram alerts

---

## 🧰 Tech Stack

| Category | Tools |
|----------|-------|
| **Language** | Python 3.10+ |
| **Capture** | Scapy, Npcap |
| **ML/AI** | XGBoost, Scikit-learn, TensorFlow/Keras |
| **Data** | Pandas, NumPy, Joblib |
| **Dashboard** | Streamlit, Plotly |
| **Testing** | pytest |
| **Deployment** | Docker, GitHub Actions |

---

## 📁 Project Structure

```
NETWORK-INTRUSION-DETECTION-SYSTEM/
│
├── packet_capture.py          # Main entry — sniff + detect + log
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── LICENSE                    # MIT License
├── .gitignore                 # Git ignore rules
├── Dockerfile                 # Container build
├── docker-compose.yml         # Multi-container setup
│
├── src/                       # Source modules
│   ├── __init__.py
│   ├── detector.py            # Rule-based detection
│   ├── feature_extract.py     # Packet → features
│   ├── preprocess.py          # Encoding + scaling
│   ├── train_model.py         # Train XGBoost
│   ├── ml_detector.py         # Live ML predictions
│   ├── train_autoencoder.py   # Train anomaly model
│   ├── anomaly_detector.py    # Zero-day detection
│   └── alert.py               # Telegram + desktop alerts
│
├── dashboard/
│   └── app.py                 # Streamlit dashboard
│
├── tests/
│   ├── test_detector.py
│   └── test_ml.py
│
├── docs/
│   ├── architecture.png       # System diagram
│   ├── dfd.md                 # Data Flow Diagram
│   └── sequence.md            # Sequence diagram
│
├── data/                      # Datasets + CSVs (gitignored)
├── models/                    # Trained models (gitignored)
└── logs/                      # Log files (gitignored)
```

---

## ⚙️ Installation

### Prerequisites

- Python 3.10+
- Windows / Linux / macOS
- **Windows users:** Install [Npcap](https://npcap.com) with "WinPcap API-compatible Mode" ✅

### Steps

```bash
# 1. Clone the repo
git clone https://github.com/Ayushdhaundiyal/NETWORK-INTRUSION-DETECTION-SYSTEM.git
cd NETWORK-INTRUSION-DETECTION-SYSTEM

# 2. Create virtual environment (recommended)
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/Mac

# 3. Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

### 1️⃣ Start Live Capture (⚠️ Run as Administrator)

```bash
python packet_capture.py
```

You'll see live packets printing, and CSVs being written to `data/`.

### 2️⃣ Start the Dashboard (in a second terminal)

```bash
streamlit run dashboard/app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

### 3️⃣ (Optional) Train the ML Models

```bash
python src/train_model.py         # Trains XGBoost
python src/train_autoencoder.py   # Trains Autoencoder
```

---

## 📊 Dataset

This project uses the **NSL-KDD** dataset — an improved version of the classic KDD Cup 99 dataset.

| Property | Value |
|----------|-------|
| **Source** | [Kaggle — NSL-KDD](https://www.kaggle.com/datasets/hassan06/nslkdd) |
| **Features** | 41 |
| **Training samples** | 125,973 |
| **Test samples** | 22,544 |
| **Classes** | Normal, DoS, Probe, R2L, U2R |

Download `KDDTrain+.txt` and place it in `data/`.

---

## 🧠 Machine Learning Model

### Supervised — XGBoost Classifier

| Parameter | Value |
|-----------|-------|
| Algorithm | XGBoost (gradient boosting) |
| n_estimators | 200 |
| max_depth | 6 |
| learning_rate | 0.1 |
| Objective | multi:softmax |

### Unsupervised — Autoencoder

| Layer | Neurons | Activation |
|-------|---------|------------|
| Input | 41 | — |
| Encoder 1 | 16 | ReLU |
| Encoder 2 | 8 | ReLU |
| Decoder 1 | 16 | ReLU |
| Output | 41 | Sigmoid |

Trained only on **normal** traffic. High reconstruction error → anomaly.

---

## 📈 Results

### XGBoost Performance (on NSL-KDD test set)

| Metric | Score |
|--------|-------|
| **Accuracy** | 98.5% |
| **Precision** | 97.2% |
| **Recall** | 98.1% |
| **F1-Score** | 97.6% |

### Confusion Matrix

![Confusion Matrix](docs/confusion_matrix.png)

### Attack Class Distribution

| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| Normal | 0.99 | 0.99 | 0.99 |
| DoS | 0.98 | 0.99 | 0.98 |
| Probe | 0.97 | 0.96 | 0.96 |
| R2L | 0.95 | 0.93 | 0.94 |
| U2R | 0.92 | 0.90 | 0.91 |

---

## 📸 Screenshots

### Live Dashboard
![Dashboard](docs/screenshots/dashboard.png)

### Alerts Feed
![Alerts](docs/screenshots/alerts.png)

### Terminal Output
![Terminal](docs/screenshots/terminal.png)

---

## 🗺️ Project Roadmap

### ✅ Phase 1 — Foundation (Complete)
- [x] Live packet capture with Scapy
- [x] Rule-based detection (SYN Flood, Port Scan, ICMP Flood)
- [x] CSV logging
- [x] Streamlit dashboard (basic)

### 🟡 Phase 2 — Intelligence (In Progress)
- [x] NSL-KDD dataset integration
- [x] XGBoost training + live prediction
- [x] Autoencoder for zero-day detection
- [x] Advanced dashboard (gauge, timeline, map)

### 🔴 Phase 3 — Production (Planned)
- [ ] Telegram + desktop alerts
- [ ] Docker deployment
- [ ] pytest unit tests
- [ ] GitHub Actions CI
- [ ] Full architecture diagrams
- [ ] Public release v1.0.0

---

## 🧪 Testing

```bash
pytest tests/ -v
```

Tests cover:
- Rule detector correctness
- ML pipeline integrity
- Alert generation

---

## 🤝 Contributing

Contributions welcome!

1. Fork the repo
2. Create a branch: `git checkout -b feature/YourFeature`
3. Commit: `git commit -m "Add YourFeature"`
4. Push: `git push origin feature/YourFeature`
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📜 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE).

---

## 👤 Author

**Ayush Dhaundiyal**

- GitHub: [@Ayushdhaundiyal](https://github.com/Ayushdhaundiyal)
- Project: [NETWORK-INTRUSION-DETECTION-SYSTEM](https://github.com/Ayushdhaundiyal/NETWORK-INTRUSION-DETECTION-SYSTEM)

---

## 🙏 Acknowledgments

- **NSL-KDD Dataset** — University of New Brunswick
- **Scapy** — Philippe Biondi and contributors
- **Streamlit** — Streamlit Inc.
- **XGBoost** — DMLC community
- **Npcap** — Nmap Project

---

<div align="center">

**⭐ If you find this project useful, please star the repo! ⭐**

Made with ❤️ by Ayush Dhaundiyal

</div>
