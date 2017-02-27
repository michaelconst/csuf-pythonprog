#!/usr/bin/python           # This is server.py file

import socket               # Import socket module


s = socket.socket()
host = socket.gethostname() # Get local machine name
port = 12350                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)
count = 2
while count > 0:
    c, (addr, port) = s.accept()
    print('Got connection from address {}, port {}'.format(addr, port))
    c.send('Hello'.encode())
    count -= 1

