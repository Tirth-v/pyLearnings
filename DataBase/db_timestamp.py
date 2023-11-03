import psycopg2
from datetime import datetime

db_params = {
    'database': 'testdb',
    'user': 'postgres',
    'password': 'admin123',
    'host': 'localhost',
}

conn = psycopg2.connect(**db_params)

cur = conn.cursor()

timestamp = datetime.now()

insert_query = "INSERT INTO details (time_stamp) VALUES (%s)"

cur.execute(insert_query, (timestamp,))

conn.commit()

cur.close()
conn.close()
