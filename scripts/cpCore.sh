#!/bin/bash

rm -r ~/ros_ws/src/baxter_examples/scripts/Alex
rm -r ~/ros_ws/src/baxter_examples/scripts/gui

mkdir -p ~/ros_ws/src/baxter_examples/scripts/Alex
mkdir -p ~/ros_ws/src/baxter_examples/scripts/gui

chmod +x ~/shared/core/*
chmod +x ~/shared/gui/*
chmod +x ~/shared/gui/baxter_custom/*
chmod +x ~/shared/gui/baxter_essentials/*
#cp ~/shared/core/* ~/ros_ws/src/baxter_examples/scripts/Alex
cp -r ~/shared/gui/* ~/ros_ws/src/baxter_examples/scripts/gui

