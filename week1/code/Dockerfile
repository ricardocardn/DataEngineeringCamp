# Usar la imagen base de Python 3.8
FROM python:3.8

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el script de ingesta al contenedor
COPY ingestion_script.py /app/script.py

# Crear la carpeta 'data' dentro del contenedor para almacenar el archivo Parquet
RUN mkdir -p /app/data

# Instalar las dependencias necesarias
RUN pip install --no-cache-dir pandas sqlalchemy pyarrow psycopg2-binary wget

# Ejecutar el script de ingesta
CMD ["python", "/app/script.py"]