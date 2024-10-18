#!/bin/bash

# Define the log file
LOG_FILE="tg_bot.log"

# Infinite loop to restart the script if it fails
while true
do
    # Run the Python module and redirect stdout and stderr to the log file
    python3 -m tg_bot

    # Check the exit status of the Python script
    EXIT_STATUS=$?
    if [ $EXIT_STATUS -ne 0 ]; then
        echo "tg_bot crashed with exit code $EXIT_STATUS. Restarting..." >> $LOG_FILE 2>&1
    else
        echo "tg_bot exited successfully. Exiting loop." >> $LOG_FILE 2>&1
        break
    fi
    
    # Optional: Add a sleep time before restarting (to avoid rapid restart loops)
    sleep 5
done