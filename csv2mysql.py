import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from os import environ, listdir
import numpy as np
from tqdm import tqdm
from mimictypes import mimic4_types

engine = create_engine(
    f'mysql+mysqldb://{environ.get("LOCAL_MYSQL_USER")}:{environ.get("LOCAL_MYSQL_PASS")}@localhost:3306/MIMICIV'
    f'?unix_socket=/var/run/mysqld/mysqld.sock')

for f in tqdm(listdir('.')):
    chunk_counter = 1
    aux = f.split('.')
    # sanity check
    if len(aux) != 2 or aux[-1].lower() != 'csv':
        continue
    print(f"Parsing file: {f}")
    table_name = aux[0]
    chunksize = 1_000_000
    for chunk in pd.read_csv(f, chunksize=chunksize, sep=',', infer_datetime_format=True, low_memory=False):
        chunk_counter += 1
        for col in chunk.columns.values:

            # ints that have missing values exceptions
            if table_name == 'd_hcpcs' and col == 'category' or\
                    table_name == 'd_items' and col == 'lownormalvalue' or\
                    table_name == 'drgcodes' and col == 'drg_severity' or\
                    table_name == 'drgcodes' and col == 'drg_mortality' or\
                    col == 'hadm_id' or col == 'pharmacy_id' or\
                    table_name == 'microbiologyevents' and col == 'org_itemid' or\
                    table_name == 'microbiologyevents' and col == 'ab_itemid' or\
                    table_name == 'microbiologyevents' and col == 'isolate_num' or\
                    table_name == 'pharmacy' and col == 'doses_per_24_hrs' or\
                    table_name == 'pharmacy' and col == 'expiration_value' or\
                    table_name == 'prescriptions' and col == 'doses_per_24_hrs':

                chunk[col] = chunk[col].fillna(-1).astype(
                    mimic4_types[table_name][col])

            else:
                chunk[col] = chunk[col].astype(mimic4_types[table_name][col])
        
        chunk.to_sql(name=table_name, con=engine,
                     if_exists='append', index=False)
