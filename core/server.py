#!/usr/bin/env python

"""
Main Server
"""

import socket               # Import socket module
import move_to_neutral
import hello

if __name__ == '__main__':
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
    ip = '192.168.1.54'  # Get local machine name
    port = 8080                 # Reserve a port for your service.
    serversocket.bind((ip, port))        # Bind to the port
    serversocket.listen(5)                 # Now wait for client connection.
    print ("Socket listening at port <%s>" % port)

    while True:
        c, addr = serversocket.accept()     # Establish connection with client.
        print 'Got connection from', addr
        num=1
        while num>0:
            num=c.recv(1024)
            if num==1:
                move_to_neutral.neutral()
            elif num==2:
                hello.sayHello()
        c.send('Thank you for connecting')
        c.close()                # Close the connection