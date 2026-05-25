import logging
import os


# EN: Create logs folder if it does not exist
# JP: logs フォルダが存在しない場合は作成
# KR: logs 폴더가 없으면 생성

os.makedirs("logs", exist_ok=True)


logging.basicConfig(
    filename="logs/system_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# EN: Log normal monitoring status
# JP: 通常の監視ステータスをログに記録
# KR: 일반 모니터링 상태를 로그에 기록

def log_status(message):
    logging.info(message)


# EN: Log warning or critical alerts
# JP: 警告または重大アラートをログに記録
# KR: 경고 또는 심각 알림을 로그에 기록

def log_alert(message):
    logging.warning(message)
