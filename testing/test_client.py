#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # Create a socket object
ip = 'localhost'         # Get local machine name
port = 8080                 # Reserve a port for your service.


s.connect((ip, port))
print "Conected to Baxter!"
s.send("1")
s.recv(1024)
s.send("2")
s.recv(1024)
s.send("3")
s.recv(1024)
s.send("1")
s.recv(1024)
s.send("0")
print(s.recv(1024))
s.close                     # Close the socket when done