#!/usr/bin/env python

"""
Move the arms to neutral position.
"""



import rospy
import baxter_interface

def move():

    rospy.init_node("Hello_Baxter")
    limb_right = baxter_interface.Limb("right")
    limb_left = baxter_interface.Limb("left")

    limb_left.set_joint_position_speed(0.2)
    limb_right.set_joint_position_speed(0.2)

    limb_right.move_to_neutral()
    limb_left.move_to_neutral()

if __name__ == '__main__':
    move()
