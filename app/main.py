import psycopg2
import time

# wait for database to start
time.sleep(5)

conn = psycopg2.connect(
    host="db",
    database="analytics",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

# create table
cur.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    product TEXT,
    amount INT
)
""")

# insert sample data
cur.execute("INSERT INTO sales (product, amount) VALUES (%s, %s)",
            ("Laptop", 1500))

cur.execute("INSERT INTO sales (product, amount) VALUES (%s, %s)",
            ("Phone", 800))

conn.commit()

cur.close()
conn.close()

print("ETL completed successfully")
