import psycopg2
import time

time.sleep(15)

conn = psycopg2.connect(
    host="db",
    database="analytics",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

cur.execute("SELECT * FROM sales")
rows = cur.fetchall()

with open("reports/output_report.csv", "w") as f:
    f.write("id,product,amount\n")
    for row in rows:
        f.write(f"{row[0]},{row[1]},{row[2]}\n")

cur.close()
conn.close()

print("Report generated successfully")
