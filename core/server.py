#!/usr/bin/env python       # This is server.py file

import socket               # Import socket module

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
   c.send('Thank you for connecting')
   c.close()                # Close the connection