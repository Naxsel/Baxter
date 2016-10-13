#!/usr/bin/env python

"""
Move the arms to neutral position.
"""

import rospy
import baxter_interface

rospy.init_node("Hello_Baxter")
limb_right = baxter_interface.Limb("right")
limb_left = baxter_interface.Limb("left")
gripper_right = baxter_interface.Gripper("right")
gripper_left = baxter_interface.Gripper("left")
head = baxter_interface.Head()

limb_left.set_joint_position_speed(1)
limb_right.set_joint_position_speed(1)

limb_right.move_to_neutral()
limb_left.move_to_neutral()

gripper_right.open()
gripper_left.open()

head.set_pan(0.0)
