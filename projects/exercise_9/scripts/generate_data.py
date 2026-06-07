from datetime import datetime
import random

LOG_FILE = "/var/log/iot-app/app.log"

try:
    # Generation start
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - Data generation started\n")

    # Simulate generating 5 records
    records = []
    for _ in range(5):
        records.append(random.randint(100, 999))

    # Generation end
    with open(LOG_FILE, "a") as log:
        log.write(
            f"{datetime.now()} - Data generation completed. Records generated: {len(records)}\n"
        )

    print(f"Generated {len(records)} records")

except Exception as e:
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - ERROR: {e}\n")

    print("Error occurred")

