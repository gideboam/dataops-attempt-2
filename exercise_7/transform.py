import csv
from datetime import datetime

INPUT_FILE = "sensor_data.csv"
OUTPUT_FILE = "cleaned_data.csv"

seen = set()
cleaned = []

with open(INPUT_FILE, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            timestamp = row["timestamp"]
            temp = int(float(row["temperature"]))
        except:
            continue

        # validate temperature
        if temp < 0 or temp > 50:
            continue

        # normalize timestamp
        try:
            dt = datetime.fromisoformat(str(timestamp))
        except:
            continue

        clean_time = dt.strftime("%Y-%m-%d %H:%M:%S")

        # remove duplicates
        key = (clean_time, temp)
        if key in seen:
            continue
        seen.add(key)

        cleaned.append([clean_time, temp])

with open(OUTPUT_FILE, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "temperature"])
    writer.writerows(cleaned)

print("Transformation complete → cleaned_data.csv created")
