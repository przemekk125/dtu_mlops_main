FROM python:3.11-slim

EXPOSE $PORT

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential git && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir fastapi pydantic uvicorn

COPY simple_fastapi_app.py simple_fastapi_app.py

CMD exec uvicorn simple_fastapi_app:app --port $PORT --host 0.0.0.0 --workers 1