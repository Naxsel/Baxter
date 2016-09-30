#!/bin/bash

# Start up script for baxter robot. Enable the baxter systems.

path= pwd

cd $HOME/ros_ws/
./baxter.sh
rosrun baxter_tools enable_robot.py -e

cd $path




