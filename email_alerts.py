import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv


# EN: Load environment variables
# JP: 環境変数を読み込む
# KR: 환경 변수를 불러오기
load_dotenv()


EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TO = os.getenv("EMAIL_TO")


# EN: Send email alert
# JP: メールアラートを送信
# KR: 이메일 알림 보내기
def send_email_alert(subject, message):
    if not all([EMAIL_HOST, EMAIL_USERNAME, EMAIL_PASSWORD, EMAIL_TO]):
        print("Email alert skipped: missing email configuration.")
        return

    email = EmailMessage()
    email["From"] = EMAIL_USERNAME
    email["To"] = EMAIL_TO
    email["Subject"] = subject
    email.set_content(message)

    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.send_message(email)

        print("Email alert sent successfully.")

    except Exception as error:
        print(f"Email alert failed: {error}")
