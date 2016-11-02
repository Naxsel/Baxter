#!/bin/bash

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu trusty main" > /etc/apt/sources.list.d/ros-latest.list'

wget http://packages.ros.org/ros.key -O - | sudo apt-key add -

sudo apt-get update
sudo apt-get -y install python build-essential git
sudo apt-get -y install ros-indigo-desktop-full
sudo rosdep init
rosdep update
sudo apt-get -y install python-rosinstall
sudo apt-get update
sudo apt-get -y install git-core python-argparse python-wstool python-vcstools python-rosdep ros-indigo-control-msgs ros-indigo-joystick-drivers gazebo2 ros-indigo-qt-build ros-indigo-driver-common ros-indigo-gazebo-ros-control ros-indigo-gazebo-ros-pkgs ros-indigo-ros-control ros-indigo-control-toolbox ros-indigo-realtime-tools ros-indigo-ros-controllers ros-indigo-xacro python-wstool ros-indigo-tf-conversions ros-indigo-kdl-parser
mkdir -p ~/ros_ws/src
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
cd ~/ros_ws/src
wstool merge https://raw.githubusercontent.com/RethinkRobotics/baxter_simulator/master/baxter_simulator.rosinstall
wstool update
source /opt/ros/indigo/setup.bash
cd ~/ros_ws
catkin_make
catkin_make install
sudo apt-get -y install ros-indigo-libfreenect ros-indigo-freenect-camera ros-indigo-freenect-launch
