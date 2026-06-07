import pandas as pd
import sqlite3

# Read the generated CSV
df = pd.read_csv("data/generated_data.csv")

# Connect to SQLite database (it will be created automatically)
conn = sqlite3.connect("data/database.db")

# Load data into table called "metrics"
df.to_sql("metrics", conn, if_exists="append", index=False)

conn.close()

print("Data loaded into database successfully")

