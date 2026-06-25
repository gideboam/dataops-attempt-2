#!/bin/bash

BACKUP_FILE=$1
DB_NAME="exercise12_db"

echo "Restoring database from $BACKUP_FILE..."

gunzip < $BACKUP_FILE | docker exec -i postgres_db_ex12 psql -U postgres $DB_NAME

echo "Restore completed."
