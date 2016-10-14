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
gripper_right.set_holding_force(100)
gripper_left.set_holding_force(30)
gripper_right.set_velocity(20)
gripper_left.set_velocity(20)

limb_left.set_joint_position_speed(0.3)
limb_right.set_joint_position_speed(0.3)

limb_right.move_to_neutral()
limb_left.move_to_neutral()


angles_right = limb_right.joint_angles()

print("Grabbing Red Cylinder")

wave_pre1_RGrab = {'right_s0': 0.220126243062, 'right_s1': -0.147645650834, 'right_e0': 0.132689338152,
                'right_e1': 0.867466135549, 'right_w0': 0.53305832379, 'right_w1': 1.57884972593, 'right_w2': 0.704864172033}
limb_right.move_to_joint_positions(wave_pre1_RGrab)

wave_pre2_RGrab = {'right_s0': 0.209388377546, 'right_s1': -0.00690291354548, 'right_e0': 0.256174791577,
                'right_e1': 0.866315649958, 'right_w0': 0.604388430427, 'right_w1': 1.58153419231, 'right_w2': 0.675335041867}
limb_right.move_to_joint_positions(wave_pre2_RGrab)

limb_right.set_joint_position_speed(0.1)

wave_RGrab = {'right_s0': 0.131155357364, 'right_s1': 0.48627190976, 'right_e0': 0.614742800745,
                'right_e1': 0.50391268882, 'right_w0': 0.526538905442, 'right_w1': 1.71192255928, 'right_w2': 0.617810762321}
limb_right.move_to_joint_positions(wave_RGrab)

rospy.sleep(3)

gripper_right.command_position(21.2317657471)

rospy.sleep(1)

# wave_post1_RGrab = {'right_s0': -0.0444854428487, 'right_s1': 0.498160260866, 'right_e0': 0.902364198474,
#                 'right_e1': 0.697961258488, 'right_w0': 0.166820410683, 'right_w1': 1.58690312507, 'right_w2': 0.623946685472}
# limb_right.move_to_joint_positions(wave_post1_RGrab)

wave_post1_RGrab = {'right_s0': 0.136140794925, 'right_s1': 0.432966077381, 'right_e0': 0.619344743109,
                'right_e1': 0.536509780563, 'right_w0': 0.506213660002, 'right_w1': 1.75410703095, 'right_w2': 0.607072896806}
limb_right.move_to_joint_positions(wave_post1_RGrab)

rospy.sleep(1)

wave_post2_RGrab = {'right_s0': 0.161834973122, 'right_s1': 0.499694241654, 'right_e0': 1.95620899975,
                'right_e1': 1.0515438301, 'right_w0': -0.769291365125, 'right_w1': 1.29583027057, 'right_w2': 1.48029146031}
limb_right.move_to_joint_positions(wave_post2_RGrab)

print("Left arm to position")
limb_left.set_joint_position_speed(0.1)

wave_pre1_LGrab = {'left_s0': -0.809941856003, 'left_s1': -0.772742821897, 'left_e0': -0.741679710943,
                   'left_e1': 0.539194246942, 'left_w0': 0.513500068745, 'left_w1': 1.91939346084, 'left_w2': -0.589815612942}
limb_left.move_to_joint_positions(wave_pre1_LGrab)

wave_LGrab = {'left_s0': -0.671883585094, 'left_s1': -0.825665159079, 'left_e0': -0.748966119685,
                   'left_e1': 1.07915548428, 'left_w0': 0.512349583154, 'left_w1': 1.43235456069, 'left_w2': -0.734776797397}
limb_left.move_to_joint_positions(wave_LGrab)

rospy.sleep(2.5)

gripper_left.command_position(16.9628429413)


rospy.sleep(1)

wave_post1_LGrab = {'left_s0': -0.571407843487, 'left_s1': -0.837937005382, 'left_e0': -0.795752533716,
                   'left_e1': 1.0131943104, 'left_w0': 0.359718494759, 'left_w1': 1.48335942189, 'left_w2': -0.693742811321}
limb_left.move_to_joint_positions(wave_post1_LGrab)

wave_post1_RGrab = {'right_s0': 0.0352815581214, 'right_s1': 0.86861662114, 'right_e0': 1.90405365296,
                'right_e1': 0.610524353578, 'right_w0': -0.695660287306, 'right_w1': 1.33839823743, 'right_w2': 0.960655468413}
limb_right.move_to_joint_positions(wave_post1_RGrab)

wave_post2_RGrab = {'right_s0': 0.0632767075003, 'right_s1': 0.966407896368, 'right_e0': 1.90673811934,
                'right_e1': 0.475917539441, 'right_w0': -0.496626280078, 'right_w1': 1.34683513176, 'right_w2': 0.78884962017}
limb_right.move_to_joint_positions(wave_post2_RGrab)

wave_post2_LGrab = {'left_s0': -0.705631162427, 'left_s1': -0.376975778623, 'left_e0': -0.902364198474,
                   'left_e1': 1.54395166301, 'left_w0': 1.10024772011, 'left_w1': 0.972160324322, 'left_w2': -1.28279143387}
limb_left.move_to_joint_positions(wave_post2_LGrab)

rospy.sleep(3)
gripper_right.open();
gripper_left.open();

wave_endL = {'left_s0': 0.253873820395, 'left_s1': -0.170271867455, 'left_e0': -1.30043221293,
                   'left_e1': 1.71690799684, 'left_w0': 1.4312040751, 'left_w1': 1.28777687143, 'left_w2': -0.822213702307}
limb_left.move_to_joint_positions(wave_endL)

wave_endR = {'right_s0': -0.27726702741, 'right_s1': 1.05729625805, 'right_e0': 2.13836921831,
                'right_e1': 0.711383590382, 'right_w0': -1.08759237861, 'right_w1': 1.52324292237, 'right_w2': 0.99401955055}
limb_right.move_to_joint_positions(wave_endR)

limb_left.move_to_neutral()
limb_right.move_to_neutral()
