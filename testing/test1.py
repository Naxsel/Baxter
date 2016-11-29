#!/usr/bin/env python

"""
Move the arms to neutral position.
"""



import rospy
import baxter_interface
import socket               # Import socket module

def move1():
    rospy.init_node("Hello_Baxter")
    limb_right = baxter_interface.Limb("right")
    limb_left = baxter_interface.Limb("left")

    limb_left.set_joint_position_speed(1)
    limb_right.set_joint_position_speed(1)

    limb_right.move_to_neutral()
    limb_left.move_to_neutral()

if __name__ == '__main__':
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
    ip = '192.168.1.52'  # Get local machine name
    print ip
    port = 8080                 # Reserve a port for your service.
    serversocket.bind((ip, port))        # Bind to the port
    serversocket.listen(5)                 # Now wait for client connection.
    while True:
       c, addr = serversocket.accept()     # Establish connection with client.
       print 'Got connection from', addr
       # script
       move1()
       c.send('Thank you for connecting')
       c.close()                # Close the connection
