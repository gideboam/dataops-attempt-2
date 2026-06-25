import csv
import psycopg2

# Connect to PostgreSQL (from your Docker setup)
conn = psycopg2.connect(
    host="localhost",
    database="testdb",
    user="admin",
    password="admin123",
    port=5433
)

cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS sensor_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    temperature INTEGER
)
""")

conn.commit()

# Read cleaned data
with open("cleaned_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cur.execute("""
            INSERT INTO sensor_data (timestamp, temperature)
            VALUES (%s, %s)
        """, (row["timestamp"], row["temperature"]))

conn.commit()

cur.close()
conn.close()

print("ETL COMPLETE: Data loaded into PostgreSQL successfully")
