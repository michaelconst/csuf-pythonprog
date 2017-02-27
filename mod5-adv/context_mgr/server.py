#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
from contextlib import closing


with closing(socket.socket()) as s:
    host = socket.gethostname() # Get local machine name
    port = 12350                # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port

    s.listen(5)
    count = 2
    while count > 0:
        with closing(s.accept()[0]) as c:
            addr, port = c.getpeername()
            print('Got connection from address {}, port {}'.format(addr, port))
            count -= 1
        c.send('Hello'.encode())
