import csv
import json
import random
import argparse
from datetime import datetime, timedelta


# CLI argument setup
parser = argparse.ArgumentParser(description="IoT Sensor Data Generator")

parser.add_argument(
    "--records",
    type=int,
    default=1000,
    help="Number of records to generate"
)

args = parser.parse_args()


# Create device list (realistic IoT devices)
devices = [f"DEV{str(i).zfill(3)}" for i in range(1, 51)]

records = []


# Generate data
for i in range(args.records):
    record = {
        "device_id": random.choice(devices),
        "temperature": round(random.uniform(15, 40), 2),
        "humidity": round(random.uniform(30, 90), 2),
        "timestamp": (datetime.now() + timedelta(seconds=i)).isoformat()
    }

    records.append(record)


# Save JSON file
with open("sensor_data.json", "w") as json_file:
    json.dump(records, json_file, indent=4)


# Save CSV file
with open("sensor_data.csv", "w", newline="") as csv_file:
    writer = csv.DictWriter(
        csv_file,
        fieldnames=["device_id", "temperature", "humidity", "timestamp"]
    )

    writer.writeheader()
    writer.writerows(records)


print(f"Generated {args.records} IoT sensor records")
print("Files created: sensor_data.csv, sensor_data.json")
