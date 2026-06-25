import csv
import random
from datetime import datetime, timedelta

data = []
start_time = datetime(2026, 6, 19, 10, 0, 0)

for i in range(20):
    timestamp = start_time + timedelta(minutes=i)
    temp = random.randint(-10, 150)

    data.append([timestamp, temp])

# Add duplicates
data.append(data[5])
data.append(data[10])

with open("sensor_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "temperature"])
    writer.writerows(data)

print("Generated sensor_data.csv successfully")
