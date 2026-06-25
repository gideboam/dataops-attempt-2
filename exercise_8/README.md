Objective
Automate the ETL pipeline to run every 10 minutes using Cron
Components
The ETL pipeline consists of:
1. generate.py - Generates IoT sensor data
2. transform.py - Cleans and validate data
3. load.py - Loads data into PostgreSQL
4. etl_pipeline.py - Ochestrates the entire ETL process
Cron schedule
The following cron job was configured:
*/10 * * * * cd /home/gideonb/dataops-attempt-2/exercise_7 && python3 etl_pipeline.py >> logs/etl.log 2>&1
Explanation
*/10 * * * * : Run every 10 minutes
cd ... : Change to the ETL working directory
python3 etl_pipeline.py : Execute the ETL pipeline




logs/etl.log : Append output to the log file

2>&1 : Redirect errors to the same log file
Logging

All ETL execution logs are stored in:

logs/etl.log

This allows monitoring and troubleshooting of automated jobs.

Validation

Cron Job:

crontab -l

Log Monitoring:

tail -20 logs/etl.log

Result

The ETL pipeline successfully runs automatically every 10 minutes and records its output in a log file.
