#!/usr/bin/env python

"""
Move the arms to neutral position.
"""

import rospy
import baxter_interface
from baxter_interface import(
    CHECK_VERSION
)

print("Initializing node... ")
rospy.init_node("Hello_Baxter")
print("Getting robot state... ")
rs = baxter_interface.RobotEnable(CHECK_VERSION)
print("Enabling robot... ")
rs.enable()




limb_right = baxter_interface.Limb("right")
limb_left = baxter_interface.Limb("left")
gripper_right = baxter_interface.Gripper("right")
gripper_left = baxter_interface.Gripper("left")
head = baxter_interface.Head()

# Verify Grippers Have No Errors and are Calibrated
print("Calibrating Grippers...")
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

print("Moving to starting position")

gripper_right.open()
gripper_left.open()
gripper_right.set_holding_force(60)
gripper_left.set_holding_force(600)
gripper_right.set_velocity(20)
gripper_left.set_velocity(20)

limb_left.set_joint_position_speed(0.3)
limb_right.set_joint_position_speed(0.3)

limb_right.move_to_neutral()
limb_left.move_to_neutral()


angles_right = limb_right.joint_angles()

print("Grabbing Red Cylinder")

wave_pre3_RGrab = {'right_s0': 0.220126243062, 'right_s1': -0.147645650834, 'right_e0': 0.132689338152,
                'right_e1': 0.867466135549, 'right_w0': 0.53305832379, 'right_w1': 1.57884972593, 'right_w2': 0.704864172033}
limb_right.move_to_joint_positions(wave_pre3_RGrab)

limb_right.set_joint_position_speed(0.1)

wave_pre4_RGrab = {'right_s0': 0.209388377546, 'right_s1': -0.00690291354548, 'right_e0': 0.256174791577,
                'right_e1': 0.866315649958, 'right_w0': 0.604388430427, 'right_w1': 1.58153419231, 'right_w2': 0.675335041867}
limb_right.move_to_joint_positions(wave_pre4_RGrab)

wave_RGrab = {'right_s0': 0.131155357364, 'right_s1': 0.48627190976, 'right_e0': 0.614742800745,
                'right_e1': 0.50391268882, 'right_w0': 0.526538905442, 'right_w1': 1.71192255928, 'right_w2': 0.617810762321}
limb_right.move_to_joint_positions(wave_RGrab)

rospy.sleep(5)

gripper_right.command_position(21.2317657471)

rospy.sleep(2)

gripper_right.open()