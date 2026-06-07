#!/bin/bash

DB_NAME="exercise10_db"
BACKUP_DIR="/opt/backups"
TIMESTAMP=$(date +%F_%H-%M-%S)
BACKUP_FILE="$BACKUP_DIR/${DB_NAME}_${TIMESTAMP}.sql.gz"

echo "Backup started at $(date)"

# Run backup as postgres user (WORKING METHOD)
sudo -u postgres pg_dump "$DB_NAME" | gzip > "$BACKUP_FILE"

if [ ${PIPESTATUS[0]} -eq 0 ]; then
    echo "Backup successful: $BACKUP_FILE"
else
    echo "Backup failed"
    rm -f "$BACKUP_FILE"
fi

echo "Backup finished at $(date)"
