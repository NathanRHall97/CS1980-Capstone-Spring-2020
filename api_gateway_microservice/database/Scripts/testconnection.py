import psycopg2

conn = psycopg2.connect(
    host='localhost',
    port=54320,
    dbname='pet_db',
    user='postgres',
    password='postgres',
)
cur = conn.cursor()
cur.execute("SELECT * FROM petTable")
result = cur.fetchall()
print(result)
conn.commit()
cur.close()
conn.close()
