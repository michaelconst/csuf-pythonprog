#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()
host = socket.gethostname() # Get local machine name
port = 12350                # Reserve a port for your service.

s.connect((host, port))
data = s.recv(1024)
print('received: {}'.format(data.decode()))
