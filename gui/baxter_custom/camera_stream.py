#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image

import std_srvs.srv

from baxter_core_msgs.srv import (
    ListCameras,
)
from baxter_interface.camera import CameraController


rospy.init_node("my_cam")
display_pub= rospy.Publisher('/robot/xdisplay',Image)
def republish(msg):
        """
            Sends the camera image to baxter's display
        """
        display_pub.publish(msg)
# left_camera = CameraController("left_hand_camera")
# left_camera.close()
right_camera = CameraController("right_hand_camera")

right_camera.resolution =(960, 600)
right_camera.open()
camera_name = "right_hand_camera"
sub = rospy.Subscriber('/cameras/' + camera_name + "/image", Image,republish,None,1)
rospy.spin()
