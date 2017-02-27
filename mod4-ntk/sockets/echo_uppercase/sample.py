import socket
from  socketserver import BaseRequestHandler, TCPServer, ThreadingMixIn
import threading


class ThreadedTCPRequestHandler(BaseRequestHandler):
    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        # send back the same message prefixed with the name of the thread handlign the request
        cur_thread = threading.current_thread()
        response = bytes('{}: {}'.format(cur_thread.name, data), 'ascii')
        self.request.sendall(response)


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass


def client(ip, port, message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    try:
        s.sendall(bytes(message, 'ascii'))
        response = str(s.recv(1024), 'ascii')
        print('received: {}'.format(response))
    finally:
        s.close()


if __name__ == '__main__':
    # "" means localhost and 0 means select an arbitrary unused port
    HOST, PORT = "", 0
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # create a thread to start the server on
    server_thread = threading.Thread(target=server.serve_forever)
    # exit the server when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print('server running on thread: {}'.format(server_thread.name))

    client(ip, port, "How ")
    client(ip, port, "are ")
    client(ip, port, "you?")

    server.shutdown()
