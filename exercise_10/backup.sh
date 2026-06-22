#!/bin/bash

echo "Starting PostgreSQL backup..."

TIMESTAMP=$(date +%F_%H-%M-%S)
BACKUP_DIR="/opt/backups"
DB_NAME="exercise12_db"

mkdir -p $BACKUP_DIR

docker exec postgres_db_ex12 pg_dump -U postgres $DB_NAME | gzip > $BACKUP_DIR/backup_$TIMESTAMP.sql.gz

echo "Backup completed: backup_$TIMESTAMP.sql.gz"
