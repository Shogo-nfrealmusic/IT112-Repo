# 1. Pythonの軽量バージョンをベースにする
FROM python:3.10-slim

# 2. 作業ディレクトリを作成・設定（/app で作業する）
WORKDIR /app

# 3. 必要ファイルをコンテナにコピー
COPY requirements.txt requirements.txt

# 4. Python依存パッケージをインストール
RUN pip install -r requirements.txt

# 5. アプリケーションのコードをすべてコピー
COPY . .

# 6. アプリを起動（Flaskがlistenするように）
CMD ["python", "app.py"]
