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

# wave_pre1_RGrab = {'right_s0': 0.108529140743, 'right_s1': -0.409189375168, 'right_e0': 0.00498543756063,
#                 'right_e1': 0.762004956382, 'right_w0': 0.236233041334, 'right_w1': 1.4944807826, 'right_w2': 0.640053483745}
# limb_right.move_to_joint_positions(wave_pre1_RGrab)
#
# wave_pre2_RGrab = {'right_s0': 0.191364103289, 'right_s1': -0.292990330486, 'right_e0': 0.0483203948184,
#                 'right_e1': 0.799970980882, 'right_w0': 0.416092288714, 'right_w1': 1.56235943246, 'right_w2': 0.727873883852}
# limb_right.move_to_joint_positions(wave_pre2_RGrab)

wave_pre3_RGrab = {'right_s0': 0.220126243062, 'right_s1': -0.147645650834, 'right_e0': 0.132689338152,
                'right_e1': 0.867466135549, 'right_w0': 0.53305832379, 'right_w1': 1.57884972593, 'right_w2': 0.704864172033}
limb_right.move_to_joint_positions(wave_pre3_RGrab)

limb_right.set_joint_position_speed(0.1)

wave_pre4_RGrab = {'right_s0': 0.209388377546, 'right_s1': -0.00690291354548, 'right_e0': 0.256174791577,
                'right_e1': 0.866315649958, 'right_w0': 0.604388430427, 'right_w1': 1.58153419231, 'right_w2': 0.675335041867}
limb_right.move_to_joint_positions(wave_pre4_RGrab)

wave_RGrab = {'right_s0': 0.164902934698, 'right_s1': 0.430281611002, 'right_e0': 0.538427256548,
                'right_e1': 0.508898126381, 'right_w0': 0.559135997184, 'right_w1': 1.72879634795, 'right_w2': 0.602087459245}
limb_right.move_to_joint_positions(wave_RGrab)

rospy.sleep(3)

gripper_right.command_position(17.6661262512)

rospy.sleep(0.5)


wave_post1_RGrab = {'right_s0': 0.136140794925, 'right_s1': 0.432966077381, 'right_e0': 0.619344743109,
                'right_e1': 0.536509780563, 'right_w0': 0.506213660002, 'right_w1': 1.75410703095, 'right_w2': 0.607072896806}
limb_right.move_to_joint_positions(wave_post1_RGrab)

wave_post2_RGrab = {'right_s0': -0.039500005288, 'right_s1': 0.363936941926, 'right_e0': 1.49908272496,
                'right_e1': 1.24981084693, 'right_w0': -0.308713633562, 'right_w1': 1.05844674364, 'right_w2': 1.28892735702}
limb_right.move_to_joint_positions(wave_post2_RGrab)

wave_post3_RGrab = {'right_s0': -0.0525388419851, 'right_s1': 0.401902966426, 'right_e0': 1.54050020623,
                'right_e1': 1.4058933921, 'right_w0': -0.390781605714, 'right_w1': 1.06803412357, 'right_w2': 1.38403416587}
limb_right.move_to_joint_positions(wave_post3_RGrab)

print("Left arm to position")
limb_left.set_joint_position_speed(0.1)

wave_pre1_LGrab = {'left_s0': -0.548781626866, 'left_s1': -1.05346130608, 'left_e0': 0.0421844716668,
                   'left_e1': 1.11213607122, 'left_w0': -0.094339818455, 'left_w1': 1.55047108136, 'left_w2': 0.11773302547}
limb_left.move_to_joint_positions(wave_pre1_LGrab)

wave_pre2_LGrab = {'left_s0': -0.474000063457, 'left_s1': -1.22680113511, 'left_e0': -0.433349572578,
                   'left_e1': 1.40896135367, 'left_w0': 0.0974077800307, 'left_w1': 1.46610213802, 'left_w2': -0.193665074471}
limb_left.move_to_joint_positions(wave_pre2_LGrab)

wave_pre3_LGrab = {'left_s0': -0.295291301668, 'left_s1': -0.733626311806, 'left_e0': -1.38671863225,
                   'left_e1': 1.40014096414, 'left_w0': 0.793835057731, 'left_w1': 1.51173806646, 'left_w2': -0.90660319034}
limb_left.move_to_joint_positions(wave_pre3_LGrab)

wave_LGrab = {'left_s0': -0.369305874683, 'left_s1': -0.804956418443, 'left_e0': -1.17848074029,
                   'left_e1': 1.44539339739, 'left_w0': 0.686839897776, 'left_w1': 1.37828173792, 'left_w2': -0.921538958322}
limb_left.move_to_joint_positions(wave_LGrab)

# rospy.sleep(1.5)
#
# gripper_left.command_position(16.4397418976)
#
# print("Opening")
#
# rospy.sleep(0.5)
# limb_left.set_joint_position_speed(0.1)
#
# wave_post1_LGrab = {'left_s0': -0.952602069277, 'left_s1': -0.952985564474, 'left_e0': -0.283019455365,
#                    'left_e1': 0.969475857944, 'left_w0': 0.16336895391, 'left_w1': 1.60377691373, 'left_w2': -0.501995212836}
# limb_left.move_to_joint_positions(wave_post1_LGrab)




