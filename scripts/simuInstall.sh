#!/bin/bash

cd ~/ros_ws/src
wstool merge https://raw.githubusercontent.com/RethinkRobotics/baxter_simulator/master/baxter_simulator.rosinstall
wstool update
source /opt/ros/indigo/setup.bash
cd ~/ros_ws
catkin_make
catkin_make install