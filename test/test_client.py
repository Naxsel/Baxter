#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # Create a socket object
ip = 'localhost'         # Get local machine name
port = 8080                 # Reserve a port for your service.

s.connect((ip, port))
print s.recv(1024)
print "Conected to Baxter!"
s.close                     # Close the socket when done