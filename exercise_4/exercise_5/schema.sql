CREATE TABLE sensor_data (
   id SERIAL PRIMARY KEY,
   device_id VARCHAR(50),
   temperature NUMERIC,
   humidity NUMERIC,
   reading_time TIMESTAMP
);
