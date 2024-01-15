FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY app/ .

CMD ["gunicorn", "config.wsgi:application", "--bind", "0:8000"]