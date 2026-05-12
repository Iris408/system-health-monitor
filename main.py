import os
import psutil
import time
from datetime import datetime
from colorama import Fore, Style, init


init(autoreset=True)

# EN: CPU warning threshold
# JP: CPU警告しきい値
# KR: CPU 경고 임계값

LOG_FILE = "logs/health_log.txt"
WARNING_THRESHOLD = 60
CRITICAL_THRESHOLD = 80
REFRESH_INTERVAL = 5

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent


def get_disk_usage():
    disk = psutil.disk_usage("/")
    return disk.percent


def get_system_uptime():
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_hours = uptime_seconds // 3600
    return int(uptime_hours)


def check_status(value):
    if value < WARNING_THRESHOLD:
        return "OK"
    elif value < CRITICAL_THRESHOLD:
        return "WARNING"
    else:
        return "CRITICAL"

def get_status_color(status):
    if status == "OK":
        return Fore.GREEN
    elif status == "WARNING":
        return Fore.YELLOW
    else:
        return Fore.RED


def save_to_log(entry):
    os.makedirs("logs", exist_ok=True)

    with open(LOG_FILE, "a") as file:
        file.write(entry + "\n")

def create_usage_bar(value, bar_length=20):
    filled_length = int(bar_length * value / 100)
    empty_length = bar_length - filled_length

    return "█" * filled_length + "-" * empty_length

def display_metric(name, value):
    status = check_status(value)
    color = get_status_color(status)
    bar = create_usage_bar(value)

    print(
        f"{name}: {value}% "
        f"[{color}{bar}{Style.RESET_ALL}] "
        f"{color}[{status}]{Style.RESET_ALL}"
    )

    return f"{name}: {value}% [{status}]"

def display_system_health():
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()
    uptime = get_system_uptime()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\nSystem Health Monitor")
    print("---------------------")
    print(f"Checked At: {current_time}")

    cpu_log = display_metric("CPU Usage", cpu)
    memory_log = display_metric("Memory Usage", memory)
    disk_log = display_metric("Disk Usage", disk)

    print(f"System Uptime: {uptime} hours")

    log_entry = (
        f"{current_time} | "
        f"{cpu_log} | "
        f"{memory_log} | "
        f"{disk_log} | "
        f"Uptime: {uptime} hours"
    )

    save_to_log(log_entry)


def clear_terminal():
    os.system("clear")


def main():
    try:
        while True:
            clear_terminal()

            print(Fore.CYAN + "System Health Monitor")
            print("-----------------------------")

            display_system_health()

            time.sleep(REFRESH_INTERVAL)

    except KeyboardInterrupt:
        print("\nSystem Health Monitor stopped.")

if __name__ == "__main__":
    main()
