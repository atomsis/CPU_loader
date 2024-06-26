SERVER_IP="127.0.0.1"
SERVER_PORT="8000"

while true; do
    cpuUsage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
    curl -X POST -d "load_percentage=$cpuUsage" http://$SERVER_IP:$SERVER_PORT/api/cpu/load/
    sleep 10
done
