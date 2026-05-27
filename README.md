# System Health Monitor 
## |  システムヘルスモニター 

A Python-based system monitoring application that tracks CPU, memory, disk usage, and uptime with threshold-based alerts, logging, Docker support, and a FastAPI dashboard.

---

## Features | 機能 

- CPU, memory, disk, and uptime monitoring
- Warning and critical threshold detection
- Slack alert integration
- Email alert integration
- Logging support
- Docker container support
- FastAPI web dashboard
- `/health` JSON endpoint
- Configurable thresholds using environment variables
- Multilingual code comments in EN/JP/KR

---

## Tech Stack | 技術スタック 

- Python
- FastAPI
- Docker
- psutil
- colorama
- Slack Webhooks
- SMTP Email
- Git/GitHub

---

## Installation

```bash

git clone https://github.com/Iris408/system-health-monitor.git
cd system-health-monitor
pip install -r requirements.txt
python3 main.py
```

---

## Docker Usage

This project can run inside a Docker container using Docker compose.

### Build and run the container

```bash
docker compose up --build
```

---

## Recent Improvements

- Added Docker container support
- Added Slack alert integration
- Added email alert integration
- Added logging support for monitoring records
- Added FastAPI web dashboard
- Added `/health` JSON endpoint
- Added configurable monitoring thresholds using environment variables
- Improved terminal compatibility for Docker
- Refined monitoring display formatting

---
