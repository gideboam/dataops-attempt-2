import argparse
import csv
import json
import random
from datetime import datetime, timedelta

def generate_data(num_records):
    data = []
    base_time = datetime.now()

    for i in range(num_records):
        record = {
            "device_id": f"device_{random.randint(1, 10)}",
            "temperature": round(random.uniform(20, 35), 2),
            "humidity": round(random.uniform(30, 80), 2),
            "timestamp": (base_time - timedelta(minutes=i)).isoformat()
        }
        data.append(record)

    return data

def save_csv(data, filename="sensor_data.csv"):
    keys = data[0].keys()
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

def save_json(data, filename="sensor_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def main():
    parser = argparse.ArgumentParser(description="IoT Sensor Data Generator")
    parser.add_argument("--records", type=int, default=1000, help="Number of records to generate")
    args = parser.parse_args()

    data = generate_data(args.records)

    save_csv(data)
    save_json(data)

    print(f"Generated {args.records} records successfully!")

if __name__ == "__main__":
    main()
