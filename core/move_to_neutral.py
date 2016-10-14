#!/usr/bin/env python

"""
Move the arms to neutral position.
"""

import rospy
import baxter_interface
from baxter_interface import CHECK_VERSION

rospy.init_node("Hello_Baxter")
limb_right = baxter_interface.Limb("right")
limb_left = baxter_interface.Limb("left")
gripper_right = baxter_interface.Gripper("right")
gripper_left = baxter_interface.Gripper("left")
head = baxter_interface.Head()

rospy.sleep(0.5)
gripper_left.open()
rospy.sleep(0.5)
gripper_right.open()

# Verify Grippers Have No Errors and are Calibrated
if gripper_left.error():
    gripper_left.reset()
if gripper_right.error():
    gripper_right.reset()
if (not gripper_left.calibrated() and
            gripper_left.type() != 'custom'):
    gripper_left.calibrate()
if (not gripper_right.calibrated() and
            gripper_right.type() != 'custom'):
    gripper_right.calibrate()

gripper_left.open()
gripper_right.open()
rospy.sleep(1)

limb_left.set_joint_position_speed(0.2)
limb_right.set_joint_position_speed(0.2)

limb_right.move_to_neutral()
limb_left.move_to_neutral()



head.set_pan(0.0)
