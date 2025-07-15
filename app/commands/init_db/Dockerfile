 Multi-stage build pour le service init_db
FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential gcc && rm -rf /var/lib/apt/lists/*

COPY ../../../../pyproject.toml ./

RUN pip install --user --upgrade pip && pip install --user --no-cache-dir .

FROM python:3.11-slim AS runtime

WORKDIR /app

COPY ../../../../app ./app
COPY ../../../../pyproject.toml ./

ENV PATH="/root/.local/bin:$PATH"

RUN pip install --user --no-cache-dir .

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["init-db"]
