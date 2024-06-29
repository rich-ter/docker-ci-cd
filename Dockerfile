FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

RUN apt-get update --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/djangocms/cms

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "cms.wsgi:application"]
