#!/usr/bin/env python       # This is server.py file

import socket               # Import socket module

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
ip = 'localhost'  # Get local machine name
print ip
port = 8080                 # Reserve a port for your service.
serversocket.bind((ip, port))        # Bind to the port

serversocket.listen(5)                 # Now wait for client connection.
while True:
    c, addr = serversocket.accept()     # Establish connection with client.
    print 'Got connection from', addr
    num = 1
    while num != "0":
        num = c.recv(1024)
        print ('Got number %s' % num)
        if num!=0:
            c.send("ok\n")
        if num == "1":
            print 1
        elif num == "2":
            print 2
    c.send('Thank you for connecting')
    print
    c.close()                # Close the connection