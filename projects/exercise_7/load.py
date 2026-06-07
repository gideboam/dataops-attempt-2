import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres",
    port=5433
)

cur = conn.cursor()

# create table
cur.execute("""
CREATE TABLE IF NOT EXISTS temperatures (
    id INT PRIMARY KEY,
    temperature INT,
    timestamp TEXT
)
""")

with open("clean_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cur.execute("""
        INSERT INTO temperatures (id, temperature, timestamp)
        VALUES (%s, %s, %s)
        """, (row["id"], row["temperature"], row["timestamp"]))

conn.commit()

cur.close()
conn.close()

print("Data successfully loaded into PostgreSQL!")
