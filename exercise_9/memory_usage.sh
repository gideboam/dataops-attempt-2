#!/bin/bash

echo "Memory Usage:"

free -m | awk 'NR==2{printf "Used: %s MB / %s MB (%.2f%%)\n", $3,$2,$3*100/$2 }'
