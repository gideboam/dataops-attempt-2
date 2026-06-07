import csv
import random
from datetime import datetime, timedelta

def generate_data(filename="data.csv", rows=30):
    base_time = datetime.now()

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        # header
        writer.writerow(["id", "temperature", "timestamp"])

        for i in range(rows):
            temperature = random.randint(-10, 50)
            timestamp = base_time + timedelta(minutes=i)

            writer.writerow([i, temperature, timestamp])

    print(f"{filename} created successfully!")

if __name__ == "__main__":
    generate_data()
