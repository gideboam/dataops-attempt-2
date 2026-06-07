import csv
from datetime import datetime

def transform_data(input_file="data.csv", output_file="clean_data.csv"):
    seen = set()
    cleaned_data = []

    with open(input_file, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row_id = row["id"]

            # 1. Remove duplicates
            if row_id in seen:
                continue
            seen.add(row_id)

            # 2. Validate temperature range
            temp = int(row["temperature"])
            if temp < -5 or temp > 45:
                continue

            # 3. Normalize timestamp
            ts = datetime.fromisoformat(row["timestamp"])
            row["timestamp"] = ts.strftime("%Y-%m-%d %H:%M:%S")

            cleaned_data.append(row)

    with open(output_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "temperature", "timestamp"])
        writer.writeheader()
        writer.writerows(cleaned_data)

    print(f"{output_file} created successfully!")

if __name__ == "__main__":
    transform_data()
