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
gripper_right.set_holding_force(50)

limb_left.set_joint_position_speed(0.6)
limb_right.set_joint_position_speed(0.6)

limb_right.move_to_neutral()
limb_left.move_to_neutral()

limb_left.set_joint_position_speed(0.1)
limb_right.set_joint_position_speed(0.1)

angles_right = limb_right.joint_angles()

print("Grabbing Red Cylinder")

wave_pre1_RGrab = {'right_s0': 0.108529140743, 'right_s1': -0.409189375168, 'right_e0': 0.00498543756063,
                'right_e1': 0.762004956382, 'right_w0': 0.236233041334, 'right_w1': 1.4944807826, 'right_w2': 0.640053483745}
limb_right.move_to_joint_positions(wave_pre1_RGrab)

wave_pre2_RGrab = {'right_s0': 0.191364103289, 'right_s1': -0.292990330486, 'right_e0': 0.0483203948184,
                'right_e1': 0.799970980882, 'right_w0': 0.416092288714, 'right_w1': 1.56235943246, 'right_w2': 0.727873883852}
limb_right.move_to_joint_positions(wave_pre2_RGrab)

wave_pre3_RGrab = {'right_s0': 0.220126243062, 'right_s1': -0.147645650834, 'right_e0': 0.132689338152,
                'right_e1': 0.867466135549, 'right_w0': 0.53305832379, 'right_w1': 1.57884972593, 'right_w2': 0.704864172033}
limb_right.move_to_joint_positions(wave_pre3_RGrab)
#
wave_pre4_RGrab = {'right_s0': 0.209388377546, 'right_s1': -0.00690291354548, 'right_e0': 0.256174791577,
                'right_e1': 0.866315649958, 'right_w0': 0.604388430427, 'right_w1': 1.58153419231, 'right_w2': 0.675335041867}
limb_right.move_to_joint_positions(wave_pre4_RGrab)

wave_RGrab = {'right_s0': 0.164902934698, 'right_s1': 0.430281611002, 'right_e0': 0.538427256548,
                'right_e1': 0.508898126381, 'right_w0': 0.559135997184, 'right_w1': 1.72879634795, 'right_w2': 0.602087459245}
limb_right.move_to_joint_positions(wave_RGrab)

rospy.sleep(0.5)

gripper_right.command_position(17.6661262512)

rospy.sleep(1)

gripper_right.command_position(96.1102142334)

rospy.sleep(0.5)

limb_right.move_to_joint_positions(wave_pre4_RGrab)
limb_right.move_to_joint_positions(wave_pre3_RGrab)
limb_right.move_to_joint_positions(wave_pre2_RGrab)
limb_right.move_to_joint_positions(wave_pre1_RGrab)
limb_right.move_to_neutral()





