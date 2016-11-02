#!/usr/bin/env python       # This is server.py file

import rospy
import socket               # Import socket module
import baxter_interface
from baxter_interface import(
    CHECK_VERSION
)

# print("Initializing node... ")
# rospy.init_node("Hello_Baxter")
# print("Getting robot state... ")
# rs = baxter_interface.RobotEnable(CHECK_VERSION)
# print("Enabling robot... ")
# rs.enable()


s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
print host
port = 8080                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   c.close()                # Close the connection