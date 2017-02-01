#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
from datetime import datetime
from time import sleep
import random


s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12350                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

# run for 10s
start = datetime.now()

try:
    while True:
        c, (addr, port) = s.accept()     # Establish connection with client.
        print('Got connection from address {}, port {}'.format(addr, port))
        elapsed = datetime.now() - start
        elapsed = elapsed.seconds * 1000 + elapsed.microseconds / 1000
        while elapsed < 100000:
            c.send('Thank you for connecting, {} with port {}'.format(addr, port).encode())
            delay = random.randint(100, 2000)
            print('delay={}'.format(delay / 1000.0))
            sleep(delay / 1000.0)
            elapsed = datetime.now() - start
            elapsed = elapsed.seconds * 1000 + elapsed.microseconds / 1000

        print('closing client connection')
        c.close()                # Close the connection
finally:
    s.close()