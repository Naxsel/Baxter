#!/usr/bin/env python

import rospy

import baxter_interface
from baxter_interface import CameraController

def sayHello():
	rospy.init_node("Hello_Baxter")
	limb_right = baxter_interface.Limb("right")
	limb_left = baxter_interface.Limb("left")
	head_camera = CameraController("head_camera")

	limb_left.set_joint_position_speed(1)
	limb_right.set_joint_position_speed(1)

	limb_right.move_to_neutral()
	limb_left.move_to_neutral()

	angles_right = limb_right.joint_angles()
	angles_left = limb_left.joint_angles()


	angles_right['right_s0']=0.0
	angles_right['right_s1']=0.0
	angles_right['right_e0']=0.0
	angles_right['right_e1']=0.0
	angles_right['right_w0']=0.0
	angles_right['right_w1']=0.0
	angles_right['right_w2']=0.0

	angles_left['left_s0']=0.0
	angles_left['left_s1']=0.0
	angles_left['left_e0']=0.0
	angles_left['left_e1']=0.0
	angles_left['left_w0']=0.0
	angles_left['left_w1']=0.0
	angles_left['left_w2']=0.0

	print angles_right
	print angles_left
	limb_right.move_to_joint_positions(angles_right)
	limb_left.move_to_joint_positions(angles_left)

	wave_1_right = {'right_s0': -0.459, 'right_s1': -0.202, 'right_e0': 1.807, 'right_e1': 1.714, 'right_w0': -0.906, 'right_w1': -1.545, 'right_w2': -0.276}

	wave_2_right = {'right_s0': -0.395, 'right_s1': -0.202, 'right_e0': 1.831, 'right_e1': 1.981, 'right_w0': -1.979, 'right_w1': -1.100, 'right_w2': -0.448}

	for _move in range(3):
		limb_right.move_to_joint_positions(wave_1_right)
		limb_right.move_to_joint_positions(wave_2_right)

	limb_right.move_to_joint_positions(angles_right)

	rospy.sleep(10)

	wave_1_left = {'left_s0': -0.459, 'left_s1': -0.202, 'left_e0': 1.807, 'left_e1': 1.714, 'left_w0': -0.906, 'left_w1': -1.545, 'left_w2': -0.276}

	wave_2_left = {'left_s0': -0.395, 'left_s1': -0.202, 'left_e0': 1.831, 'left_e1': 1.981, 'left_w0': -1.979, 'left_w1': -1.100, 'left_w2': -0.448}


	for _move in range(3):
		limb_left.move_to_joint_positions(wave_1_left)
		limb_left.move_to_joint_positions(wave_2_left)

	limb_left.move_to_joint_positions(angles_left)

	limb_right.move_to_neutral()
	limb_left.move_to_neutral()

	quit()

if __name__ == '__main__':
    sayHello()
