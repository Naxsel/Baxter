#!/usr/bin/env python

import argparse
import socket
import sys

import rospy
import rosgraph

import std_srvs.srv

from baxter_core_msgs.srv import (
    ListCameras,
)
from baxter_interface.camera import CameraController
from sensor_msgs.msg import Image

try:
        reset_srv = rospy.ServiceProxy('cameras/reset', std_srvs.srv.Empty)
        rospy.wait_for_service('cameras/reset', timeout=10)
        reset_srv()
except:
        srv_ns = rospy.resolve_name('cameras/reset')
        rospy.logerr("Failed to call reset devices service at %s", srv_ns)
        raise
else:
        ls = rospy.ServiceProxy('cameras/list', ListCameras)
        rospy.wait_for_service('cameras/list', timeout=10)
        resp = ls()
        if len(resp.cameras):
                # Find open (publishing) cameras
                master = rosgraph.Master('/rostopic')
                resp.cameras
                cam_topics = dict([(cam, "/cameras/%s/image" % cam)
                                   for cam in resp.cameras])
                open_cams = dict([(cam, False) for cam in resp.cameras])
                try:
                        topics = master.getPublishedTopics('')
                        for topic in topics:
                                for cam in resp.cameras:
                                        if topic[0] == cam_topics[cam]:
                                                open_cams[cam] = True
                except socket.error:
                        raise ROSTopicIOException("Cannot communicate with master.")
                for cam in resp.cameras:
                        print("%s%s" % (cam, ("  -  (open)" if open_cams[cam] else "")))
        else:
                print ('No cameras found')

rospy.init_node("my_cam")
display_pub= rospy.Publisher('/robot/xdisplay',Image)
def republish(msg):
        """
            Sends the camera image to baxter's display
        """
        display_pub.publish(msg)
left_camera = CameraController("left_hand_camera")
left_camera.close()
head_camera = CameraController("head_camera")

head_camera.resolution =(960, 600)
head_camera.open()
camera_name = "head_camera"
sub = rospy.Subscriber('/cameras/' + camera_name + "/image", Image,republish,None,1)
rospy.spin()

