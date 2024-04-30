SERVER_IP="127.0.0.1"
SERVER_PORT="8001"

while true; do
    cpuUsage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
#   cpuUsage=$(top -bn1 | awk '/Cpu/ { print $2}')
    curl -X POST -d "load_percentage=$cpuUsage" http://$SERVER_IP:$SERVER_PORT/api/cpu/load/
    sleep 10
done

#!/bin/bash
# This script monitors CPU and memory usage

#while true; do
#  # Get the current usage of CPU and memory
#  cpuUsage=$(top -bn1 | awk '/Cpu/ { print $2}')
#  memUsage=$(free -m | awk '/Mem/{print $3}')
#
#  # Print the usage
#  echo "CPU Usage: $cpuUsage%"
#  echo "Memory Usage: $memUsage MB"
#
#  # Sleep for 1 second
#  sleep 1
#done