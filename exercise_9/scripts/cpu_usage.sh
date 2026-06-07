#!/bin/bash

echo "CPU Usage Report"
top -bn1 | grep "Cpu(s)"
