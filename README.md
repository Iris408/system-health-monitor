# System Health Monitor

A Python-based system monitoring application that tracks CPU, memory, disk usage, and system uptime with real-time status monitoring and color-coded alerts.

---

# Features

- Monitor CPU usage
- Monitor memory usage
- Monitor disk usage
- Track system uptime
- Warning and critical threshold detection
- Color-coded monitoring output
- Dynamic status messages
- Modular helper functions
- Multilingual code comments (EN/JP/KR)

---

# Technologies Used

- Python
- Docker
- Slack
- psutil
- colorama
- Git/GitHub

---

# Docker Support

Run with Docker:

```bash
docker build -t system-health-monitor .
docker run system-health-monitor
```

---

# Docker Compose 

Run with Docker Compose:

```bash
docker compose up
```

---


# Project Structure

```bash
system-health-monitor/ │ ├── main.py ├── requirements.txt ├── README.md 
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Iris408/system-health-monitor.git 
```

Navigate into project:

```bash
cd system-health-monitor 
```

Install dependencies:

```bash
pip install -r requirements.txt 
```

Run the application:

```bash
python3 main.py 
```

---

# Example Output

```plaintext
System Health Monitor
----------------------

CPU Usage: 5.9% [OK]
Memory Usage: 78.4% [WARNING]
Disk Usage: 8.4% [OK]
```

---

# Monitoring Logic

| Status | Condition |
|---|---|
| OK | Below warning threshold |
| WARNING | Above warning threshold |
| CRITICAL | Above critical threshold |

---

# Recent Improvements

- Added Docker support
- Added Slack alert integration
- Improved terminal compatibility
- Refined monitoring display formatting

---

# Future Improvements

- Email alerts
- Cloud deployment
- Configurable alert thresholds
- Historical logging
- Grafana-style metrics dashboard
- FastAPI Web dashboard

---

# English / 日本語 / 한국어

## EN
System monitoring application built with Python.

## JP
Python を使用したシステム監視アプリケーション。

## KR
Python 기반 시스템 모니터링 애플리케이션.
