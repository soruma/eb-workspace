FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync

COPY src/ ./src/

EXPOSE 8000

CMD ["uv", "run", "python", "src/manage.py", "runserver", "0.0.0.0:8000"]
