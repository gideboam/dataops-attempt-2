CREATE TABLE sensor_data (
    id SERIAL PRIMARY KEY,
    device_id VARCHAR(50),
    temperature NUMERIC,
    humidity NUMERIC,
    reading_time TIMESTAMP
);

INSERT INTO sensor_data (device_id, temperature, humidity, reading_time)
VALUES
('DEV001', 25.5, 60.2, '2026-06-07 08:00:00'),
('DEV001', 27.1, 58.4, '2026-06-07 10:00:00'),
('DEV002', 30.2, 55.0, '2026-06-07 09:00:00'),
('DEV002', 31.8, 54.1, '2026-06-08 09:00:00'),
('DEV003', 22.4, 70.3, '2026-06-08 11:00:00');

-- Avg temperature per device
SELECT device_id, AVG(temperature)
FROM sensor_data
GROUP BY device_id;

-- Max temperature per day
SELECT DATE(reading_time), MAX(temperature)
FROM sensor_data
GROUP BY DATE(reading_time);

-- Count per device
SELECT device_id, COUNT(*)
FROM sensor_data
GROUP BY device_id;
