-- Average temperature per device
SELECT
    device_id,
    AVG(temperature) AS avg_temperature
FROM sensor_data
GROUP BY device_id;

-- Max temperature per day
SELECT
    DATE(reading_time) AS day,
    MAX(temperature) AS max_temperature
FROM sensor_data
GROUP BY DATE(reading_time)
ORDER BY day;

-- Count readings per device
SELECT
    device_id,
    COUNT(*) AS reading_count
FROM sensor_data
GROUP BY device_id
ORDER BY reading_count DESC;
