#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import select

host = socket.gethostname() # Get local machine name
port = 12350                # Reserve a port for your service.

s1 = socket.socket()         # Create a socket object
s1.connect((host, port))
s2 = socket.socket()         # Create another socket object
s2.connect((host, port))

rlist = [s1, s2]
while True:
    descriptors = select.select(rlist, [], [], 10)
    if any(descriptors):
        print('looping...')
        for s in descriptors[0]:
            try:
                data = s.recv(1024)
                if data:
                    print(data.decode())
                else:
                    # server closed the socket
                    print('connection closed')
                    rlist.remove(s)
            except Exception as e:
                s.close()
    else:
        print('10s timeout')
