#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image

import std_srvs.srv

from baxter_core_msgs.srv import (
    ListCameras,
)
from baxter_interface.camera import CameraController

"""
    Sends the camera image to baxter's display
"""
def run():
    rospy.init_node("my_cam")
    display_pub= rospy.Publisher('/robot/xdisplay',Image)
    def republish(msg):
        display_pub.publish(msg)

    # Change for left camera if desired
    # camera = CameraController("left_hand_camera")
    camera = CameraController("right_hand_camera")

    camera.resolution =(960, 600)
    camera.open()
    # camera_name = "left_hand_camera")
    camera_name = "right_hand_camera"
    sub = rospy.Subscriber('/cameras/' + camera_name + "/image", Image,republish,None,1)
    rospy.spin()


if __name__ == '__main__':
    run()