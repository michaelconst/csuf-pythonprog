import socket
import select
import os


class ChatServer:
    def __init__(self, port):
        self.port = port
        self.srvsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # to enable the server to be restarted
        self.srvsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.srvsocket.bind(('', self.port))
        self.srvsocket.listen(5)
        self.descriptors = [self.srvsocket]
        print('ChatServer started on port {}'.format(self.port))

    def run(self):
        while True:
            lread, lwrite, lexc = select.select(self.descriptors, [], [])
            for s in lread:
                if s == self.srvsocket:
                    # received a client connection
                    self.accept_new_connection()
                else:
                    # received client message
                    # get client info
                    host, port = s.getpeername()
                    msg = s.recv(100)
                    if len(msg) == 0:
                        # client closed the connection
                        client_quit_msg = 'client at {}:{} left'.format(host, port)
                        self.broadcast_string(client_quit_msg, s)
                        self.descriptors.remove(s)
                    else:
                        # broadcast the message
                        msg = msg.decode()[:-2]
                        client_msg = '[{}:{}] {}'.format(host, port, msg)
                        self.broadcast_string(client_msg, s)

    def broadcast_string(self, msg, omit_sock):
        for s in self.descriptors:
            if s != omit_sock and s != self.srvsocket:
                s.send((msg + os.linesep).encode())
                print(msg)

    def accept_new_connection(self):
        c, (host, port) = self.srvsocket.accept()
        self.descriptors.append(c)
        c.send(("you're connected to the Python chat server" + os.linesep).encode())
        client_msg = 'client {}:{} joined'.format(host, port)
        self.broadcast_string(client_msg, c)


if __name__ == '__main__':
    server = ChatServer(2626)
    server.run()