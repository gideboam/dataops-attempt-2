import os
import time
import psycopg2

db_host = os.getenv("DB_HOST", "localhost")
db_name = os.getenv("DB_NAME", "exercise12_db")
db_user = os.getenv("DB_USER", "postgres")
db_password = os.getenv("DB_PASSWORD", "postgres")

time.sleep(5)  # wait for DB

conn = psycopg2.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id SERIAL PRIMARY KEY,
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

cur.execute("INSERT INTO logs (message) VALUES ('ETL job ran successfully');")

conn.commit()

cur.execute("SELECT * FROM logs;")
rows = cur.fetchall()

print("=== REPORT ===")
for row in rows:
    print(row)

cur.close()
conn.close()
