#!/bin/bash

LOG_FILE="logs/pipeline.log"

echo "Pipeline started at $(date)" >> $LOG_FILE

python3 scripts/generate_data.py >> $LOG_FILE 2>&1
python3 scripts/load_to_db.py >> $LOG_FILE 2>&1

echo "Pipeline finished at $(date)" >> $LOG_FILE
echo "------------------------" >> $LOG_FILE
