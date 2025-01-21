FROM python:3.8

WORKDIR /app
COPY ingestion_script.py /app/script.py
RUN mkdir -p /app/data

RUN pip install --no-cache-dir pandas sqlalchemy pyarrow psycopg2-binary wget

CMD ["python", "/app/script.py"]
