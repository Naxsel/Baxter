#!/bin/bash

# Start up script for baxter robot. Enable the baxter systems.

state="$(rosrun baxter_tools enable_robot.py -s | grep enable | grep True)"

if [ -n "$state" ]; then #True if string is not empty
    echo "Baxter enabled, disabling..."
    rosrun baxter_tools enable_robot.py -d
else
    echo "Baxter not enabled, starting..."
    rosrun baxter_tools enable_robot.py -e
fi
