from datetime import datetime

LOG_FILE = "/var/log/iot-app/app.log"

try:
    inserted_count = 5 / 0

    with open(LOG_FILE, "a") as log:
        log.write(
            f"{datetime.now()} - Database insert completed. Records inserted: {inserted_count}\n"
        )

    print(f"Inserted {inserted_count} records")

except Exception as e:
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - ERROR: {e}\n")

    print("Error occurred")

