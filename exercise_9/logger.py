import logging

logging.basicConfig(
    filename="/var/log/iot-app/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()

logger.info("Generation started")

records_inserted = 1000
logger.info(f"Inserted {records_inserted} records")

logger.info("Generation completed")

try:
    x = 10 / 0
except Exception as e:
    logger.error(f"Error occurred: {e}")
