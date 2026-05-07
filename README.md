# System Health Monitor

A Python-based command-line tool that monitors system health metrics such as CPU usage, memory usage, disk usage, and system uptime.

## Features

- Monitors CPU, memory, and disk usage
- Displays system uptime
- Uses status levels: OK, WARNING, and CRITICAL
- Shows colored terminal output
- Displays visual usage bars
- Logs system health checks to a file
- Refreshes automatically every 5 seconds
- Handles clean shutdown with `Ctrl + C`

## Technologies Used

- Python
- psutil
- colorama

## Project Structure

```text
system-health-monitor/
├── logs/
│   └── health_log.txt
├── README.md
├── requirements.txt
└── main.py
