import pandas as pd
from sqlalchemy import create_engine
import pyarrow.parquet as pq

from time import time
import os

host = 'pgdatabase'

def ingest_data(user, password, db, file):
    engine = create_engine(f'postgresql://{password}:{user}@{host}:5432/{db}', echo=False)

    pf = pq.ParquetFile(file)
    for i, batch in enumerate(pf.iter_batches(batch_size=100000)):
        start = time()
        batch.to_pandas().to_sql('taxi', engine, if_exists='append')
        print(f'Batch: {i}. Elapsed time: {time() - start:.2f} sec')


if __name__ == '__main__':
    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    db = os.getenv('POSTGRES_DB')

    url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet'
    output_file = './data/yellow_tripdata_2024-01.parquet'
    os.system(f'wget {url} -O {output_file}')
    # comprobar si se descargó el archivo
    if os.path.isfile(output_file):
        print('File downloaded')

    ingest_data(user, password, db, output_file)
