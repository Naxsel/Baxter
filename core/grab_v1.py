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

gripper_right.open()
gripper_left.open()

limb_left.set_joint_position_speed(1)
limb_right.set_joint_position_speed(1)

limb_right.move_to_neutral()
limb_left.move_to_neutral()

limb_left.set_joint_position_speed(0.1)
limb_right.set_joint_position_speed(0.1)

angles_right = limb_right.joint_angles()

angles_right['right_s0']=0.0
angles_right['right_s1']=0.0
angles_right['right_e0']=0.0
angles_right['right_e1']=0.0
angles_right['right_w0']=0.0
angles_right['right_w1']=0.0
angles_right['right_w2']=0.0

# wave_1_right = {'right_s0': 0, 'right_s1': 0, 'right_e0': 0,
#                  'right_e1': 0, 'right_w0': 0, 'right_w1': 0, 'right_w2': 0}

wave_1_right = {'right_s0': 0.110063121531, 'right_s1': 0.151864098001, 'right_e0': 0.154932059576,
                'right_e1': 0.989801103383, 'right_w0': 0.927291386277, 'right_w1': 1.62870410154, 'right_w2': 0.530373857411}

limb_right.move_to_joint_positions(wave_1_right)

wave_2_right = {'right_s0': 0.080917486561, 'right_s1': 0.384262187365, 'right_e0': 0.727490388655,
                'right_e1': 0.912335073595, 'right_w0': 0.370456360274, 'right_w1': 1.35795649248, 'right_w2': 0.592883574518}

limb_right.move_to_joint_positions(wave_2_right)

gripper_right.command_position(9.07617473602)

# wave_3_right = {'right_s0': 0.080917486561, 'right_s1': 0.384262187365, 'right_e0': 0.727490388655,
#                 'right_e1': 0.912335073595, 'right_w0': 0.370456360274, 'right_w1': 1.35795649248, 'right_w2': 0.592883574518}
#
# limb_right.move_to_joint_positions(wave_3_right)


