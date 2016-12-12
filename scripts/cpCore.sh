#!/bin/bash

rm -r ~/ros_ws/src/baxter_examples/scripts/Alex
mkdir -p ~/ros_ws/src/baxter_examples/scripts/Alex
chmod +x ~/shared/core/*
cp ~/shared/core/* ~/ros_ws/src/baxter_examples/scripts/Alex
