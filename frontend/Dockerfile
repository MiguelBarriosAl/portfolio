FROM python:3.11-slim

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN apt-get update && apt-get install -y curl build-essential \
 && curl -sSL https://install.python-poetry.org | python3 - \
 && ln -s /root/.local/bin/poetry /usr/local/bin/poetry \
 && poetry config virtualenvs.create false \
 && poetry install --no-root --no-ansi --no-interaction

COPY . .

CMD ["poetry", "run", "streamlit", "run", "frontend/Home.py"]
