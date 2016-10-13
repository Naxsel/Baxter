#!/bin/bash

sudo rm -r ~/ros_ws/src
mkdir -p ~/ros_ws/src
rosdep update
source /opt/ros/indigo/setup.bash
cd ~/ros_ws
catkin_make
catkin_make install
cd ~/ros_ws/src
wstool init .
wstool merge https://raw.githubusercontent.com/RethinkRobotics/baxter/master/baxter_sdk.rosinstall
wstool update
source /opt/ros/indigo/setup.bash
cd ~/ros_ws
catkin_make
catkin_make install
cp ~/Dropbox/JetBrains/Baxter/baxter.sh .
cp ~/Dropbox/JetBrains/Baxter/core/AB.py ~/ros_ws/src/baxter_examples/scripts/
cp ~/Dropbox/JetBrains/Baxter/core/move_to_neutral.py ~/ros_ws/src/baxter_examples/scripts/


