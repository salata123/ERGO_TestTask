FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /data/input
RUN mkdir -p /data/output

VOLUME ["/data/input"]
VOLUME ["/data/output"]

COPY test_files /data/input

CMD ["python", "-m", "app.app"]
