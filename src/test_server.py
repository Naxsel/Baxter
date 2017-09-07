#!/usr/bin/env python

import socket               # Import socket module
import thread
import time
# import rospy
# import baxter_interface
# from baxter_interface import CHECK_VERSION
# import baxter_essentials
import baxter_custom

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
# ip = "192.168.1.4"  # Get local machine name
ip = "localhost"
port = 8080                 # Reserve a port for your service.
serversocket.bind((ip, port))        # Bind to the port

serversocket.listen(5)                 # Now wait for client connection.
while True:
    print("Waiting for Connection...")
    c, addr = serversocket.accept()     # Establish connection with client.
    print 'Got connection from', addr
    c.send("connected");
    code = "es1"
    while code != "0":
        code = c.recv(1024)
        print ('Got code %s' %code)

        if code == "es1":
            c.send("ok")
            # thread.start_new_thread(baxter_custom.move_to_neutral.run(), [])
        elif code == "es2":
            c.send("ok")
            # thread.start_new_thread(baxter_custom.joint_wobbler.main(), [])
        elif code == "es3":
            c.send("ok")
            # thread.start_new_thread(baxter_custom.head_wobbler.main(), [])
        elif code == "cs1":
            c.send("ok")
            # thread.start_new_thread(baxter_custom.hello.run(), [])
        elif code == "cs2":
            c.send("ok")
            # thread.start_new_thread(baxter_custom.open_cylinder.run(), [])
        elif code == "cs3":
            c.send("ok")
            # thread.start_new_thread(baxter_custom.camera_stream.run(), [])
    print("Disconnected")
    c.send('Thank you for connecting')
    c.close()                # Close the connection