# Exercise 8 - Automation with Cron

## Overview
This project demonstrates an automated data pipeline using Cron jobs. The pipeline generates data, loads it into a database, and logs execution results.

---

## Components

### 1. Data Generation
- Script: `scripts/generate_data.py`
- Generates random sample data
- Saves output to `data/generated_data.csv`

### 2. Data Loading
- Script: `scripts/load_to_db.py`
- Loads CSV data into SQLite database (`data/database.db`)

### 3. Pipeline Automation
- Script: `scripts/pipeline.sh`
- Runs both generation and loading scripts
- Logs output to `logs/pipeline.log`

---

## Scheduling (Cron Job)

The pipeline runs automatically every 10 minutes:

```bash
*/10 * * * * /bin/bash /root/iot-app/exercise_8/scripts/pipeline.sh

