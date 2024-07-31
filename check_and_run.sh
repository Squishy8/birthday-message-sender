#!/bin/bash

LOGFILE="path/to/cron_run.log"
TODAY=$(date +%Y-%m-%d)


# Set DISPLAY variable
export DISPLAY=:0

# Check if the cron job has already run today
if [ -e "$LOGFILE" ]; then
  LAST_RUN=$(cat "$LOGFILE")
  if [ "$LAST_RUN" == "$TODAY" ]; then
    exit 0
  fi
fi

# Sleep for 20 seconds to simulate delay (if necessary)
sleep 20

# Run the Python script
python3 path/to/birthday.py

# Update the log file with today's date
echo "$TODAY" > "$LOGFILE"

