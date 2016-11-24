#!/usr/bin/env python

"""
Main Server
"""

import socket               # Import socket module
import time

if __name__ == '__main__':
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
    ip = 'localhost'  # Get local machine name
    port = 8080                 # Reserve a port for your service.
    serversocket.bind((ip, port))        # Bind to the port
    serversocket.listen(5)                 # Now wait for client connection.
    print ("Socket listening at port <%s>" % port)

    while True:
        c, addr = serversocket.accept()     # Establish connection with client.
        print 'Got connection from', addr
        c.send("Conected to Baxter!")
        code=c.recv(1024)
        if code=="0":
            c.send('Thank you for connecting')
            c.close()  # Close the connection
            c, addr = serversocket.accept()  # Establish connection with client.
            print 'Got connection from', addr
            c.send("Conected to Baxter!")
        elif code =="1":
            c.send('Option 1 selected')
            time.sleep(5)
        elif code =="2":
            c.send('Option 2 selected')
            time.sleep(5)
        elif code =="3":
            c.send('Option 3 selected')
            time.sleep(5)
        elif code =="4":
            c.send('Option 4 selected')
            time.sleep(5)
        elif code =="5":
            c.send('Option 5 selected')
            time.sleep(5)
        elif code =="6":
            c.send('Option 6 selected')
            time.sleep(5)
        elif code =="7":
            c.send('Option 7 selected')
            time.sleep(5)
        else :
            print "option not listed, listening again"
            c.send('error')
