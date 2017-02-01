from tkinter import *
from PIL import Image, ImageTk
import socket, asyncore

from tic_tac_toe import Game


X_FILE = 'images/x.png'
O_FILE = 'images/o.png'
# use a grid image
GRID_FILE = 'images/grid.png'

PORT = 9778
MSG_HELLO = 1
MSG_HELLO_ACK = 2
MSG_MOVE = 3
MSG_MOVE_ACK = 4

PLAYER1 = 1
PLAYER2 = 2


class RemoteGame(Game, asyncore.dispatcher):
    def __init__(self, master, player1=True, host='localhost', port=PORT, player1_img=X_FILE, player2_img=O_FILE):
        Game.__init__(master, player1=player1, player1_img=player1_img, player2_img=player2_img)
        self.host = host
        self.port = port
        self.player1_turn = player1
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            self.send('%d!%d' % (MSG_HELLO, PLAYER1))
        except Exception as e:
            print('send error: {}'.format(str(e)))
            # bind to socket
            self.set_reuse_addr()
            self.bind((host, port))
            prompt = 'Waiting for %s' % ('player2' if self.player1_turn else 'player1')
            self.player.config(text=prompt)

    def handle_read(self):
        data = self.recv(1024)
        msg = str(data)
        parts = msg.split('!')
        msg_type = int(parts[0])
        if msg_type == MSG_HELLO:
            # other player connected to us, ignore his player choice
            # send acknowledgement
            player = PLAYER1 if self.player1_turn else PLAYER2
            msg = '%d!%d' % (MSG_HELLO_ACK, player)
            prompt = 'Waiting for %s' % ('player2' if self.player1_turn else 'player1')
            self.player.config(text=prompt)
        elif msg == MSG_HELLO_ACK:
            # the other player was waiting
            player = int(parts[1])
            self.player1_turn = (player == PLAYER2)
            prompt = 'Waiting for %s' % ('player2' if self.player1_turn else 'player1')
            self.player.config(text=prompt)
        # TODO handle MOVE message


if __name__ == '__main__':
    root = Tk()
    grid_image = ImageTk.PhotoImage(Image.open(GRID_FILE))
    game = Game(root)
    mainloop()
