FROM python:3.11-slim

# Evitar archivos pyc y buffers
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.7.1

# Instalar Poetry y dependencias básicas
RUN apt-get update \
  && apt-get install -y curl build-essential \
  && curl -sSL https://install.python-poetry.org | python3 - \
  && ln -s /root/.local/bin/poetry /usr/local/bin/poetry \
  && apt-get purge -y curl \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
  && poetry install --no-root --no-ansi --no-interaction

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
