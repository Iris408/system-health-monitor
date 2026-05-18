# EN: Python base image
# JP: Python ベースイメージ
# KR: Python 기본 이미지

FROM python:3.11


# EN: Set working directory
# JP: 作業ディレクトリ設定
# KR: 작업 디렉토리 설정

WORKDIR /app


# EN: Copy project files
# JP: プロジェクトファイルコピー
# KR: 프로젝트 파일 복사

COPY . .


# EN: Install dependencies
# JP: 依存関係インストール
# KR: 의존성 설치

RUN pip install -r requirements.txt


# EN: Run application
# JP: アプリ実行
# KR: 애플리케이션 실행

CMD ["python", "main.py"]
