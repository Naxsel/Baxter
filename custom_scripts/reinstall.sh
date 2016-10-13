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
mkdir -p ~/ros_ws/src/baxter_examples/scripts/Alex
cp ~/Dropbox/JetBrains/Baxter/baxter.sh .
cp ~/Dropbox/JetBrains/Baxter/custom_scripts/startStop.sh .
cp ~/Dropbox/JetBrains/Baxter/core/* ~/ros_ws/src/baxter_examples/scripts/Alex



