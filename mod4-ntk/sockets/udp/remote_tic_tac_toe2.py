from tkinter import *
from PIL import Image, ImageTk
import socket
import argparse
import random

from tic_tac_toe import Game, PLAYER1, PLAYER2


X_FILE = 'images/x.png'
O_FILE = 'images/o.png'
# use a grid image
GRID_FILE = 'images/grid.png'

PORT = 5005
MAX_PORT = 65535
MSG_HELLO = 1
MSG_MOVE = 2


class GameState:
    def is_end_state(self):
        return False

    def transition(self, input, game):
        print('transition, current input={}, current state={}'.format(input, game.state))
        next_states = [(s, g) for f, g, s in self.map if f(input, game)]
        assert len(next_states) == 1, "faulty transition rule"
        s, g = next_states[0]
        game.state = eval(s)()
        print('transition, executing {}'.format(g.__name__))
        next_input = g(input, game)
        print('transition, next input={}, next state={}'.format(next_input, game.state))
        return next_input

    def run(self, input, game):
        event = input
        while not game.state.is_end_state():
            event = game.state.transition(event, game)

    def send_hello_and_wait(self, _, game):
        msg = '%d!%d!%d!%d' % (MSG_HELLO, game.player, game.token, game.recv_port)
        game.socket.sendto(msg.encode(), (game.host, game.port))
        print('Player {} sent Hello {} to host={}, port={}'.format(game.player, msg, game.host, game.port))
        try:
            data, addr = game.socket.recvfrom(1024)
            if game.remote is None:
                game.remote = addr
            msg = data.decode()
            print('received {}'.format(msg))
            parts = msg.split('!')
            token = int(parts[2])
            if game.token == token:
                # continue sending and waiting
                return "timeout"
            else:
                return msg
        except socket.timeout as e:
            print('recvfrom timeout: {}'.format(str(e)))
            # continue sending and waiting
            return "timeout"


class StartState(GameState):
    def __init__(self):
        self.map = [(self.init_game, self.send_hello_and_wait, 'WaitingState')]

    def init_game(self, _, game):
        assert not game.is_bound, "socket should not be bound"
        # bind to socket
        game.socket.bind(('', game.port))
        game.handshake_socket.bind('', PORT)
        prompt = 'Waiting...'
        game.lbl_player.config(text=prompt)
        return True


class WaitingState(GameState):
    def __init__(self):
        self.map = [(lambda input, _: input == "timeout", self.send_hello_and_wait, 'WaitingState'),
                    (self.check_hello, self.send_hello, 'ReadyState')]

    def check_hello(self, input, game):
        if input is None:
            return False
        try:
            parts = input.split('!')
            msg_type = int(parts[0])
            token = int(parts[2])
            match = msg_type == MSG_HELLO and game.token != token
            if match:
                if game.token < token:
                    game.player = PLAYER1
                else:
                    game.player = PLAYER2
            return match
        except (ValueError, IndexError):
            return False

    def send_hello(self, _, game):
        for i in range(3):
            msg = '%d!%d!%d' % (MSG_HELLO, game.player, game.token)
            game.socket.sendto(msg.encode(), (game.host, game.port))
            print('Player {} sent Hello {} to host={}, port={}'.format(game.player, msg, game.host, game.port))
        prompt = 'Player' + str(game.player)
        game.lbl_player.config(text=prompt)


class ReadyState(GameState):
    def is_end_state(self):
        return True


class RemoteGame(Game):
    def __init__(self, master, host='127.0.0.1', player1_img=X_FILE, player2_img=O_FILE):
        Game.__init__(self, master, player1_img=player1_img, player2_img=player2_img)
        self.host = host
        self.port = random.randint(self.port+1, min(self.port+1000, MAX_PORT))
        self.token = random.randint(1, 1000000)
        self.handshake_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.handshake_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if hasattr(socket, "SO_REUSEPORT"):
            self.handshake_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.handshake_socket.settimeout(1)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if hasattr(socket, "SO_REUSEPORT"):
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.socket.settimeout(1)
        self.remote = None
        self.is_bound = False
        self.is_ready = False
        self.state = StartState()
        self.state.run(None, self)

    def _is_my_turn(self):
        return self.player == PLAYER1 and self.player1_turn or self.player == PLAYER2 and not self.player1_turn

    def _flip(self):
        self.player = PLAYER1 if self.player == PLAYER2 else PLAYER2
        self.player1_turn = not self.player1_turn

    def _get_widget(self, row, col):
        for name, w in self.frame.children.items():
            if name[4:] == '%d%d' % (row, col):
                return w
        else:
            return None

    def process_move(self, w, row, col):
        if not self.is_ready:
            return
        if self._is_my_turn():
            self.send_move(w, row, col)
        else:
            super().process_move(w, row, col)

    def send_move(self, row, col):
        msg = ('%d!%d%d,%d' % (MSG_MOVE, self.player, row, col)).encode()
        self.socket.sendto(msg, (self.host, self.port))
        print('sent move {}'.format(msg))
        self.wait_move_ack(row, col)

    def send_move_ack(self, row, col):
        msg = ('%d!%d%d,%d' % (MSG_MOVE_ACK, self.player, row, col)).encode()
        self.socket.sendto(msg, (self.host, self.port))
        print('sent move ack {}'.format(msg))

    def send_hello(self):
        msg = '%d!%d!%d' % (MSG_HELLO, self.player, self.token)
        self.socket.sendto(msg.encode(), (self.host, self.port))
        print('Player {} sent Hello {} to host={}, port={}'.format(self.player, msg, self.host, self.port))

    def send_hello_ack(self):
        msg = ('%d!%d!%d' % (MSG_HELLO_ACK, self.player, self.token)).encode()
        self.socket.sendto(msg, self.remote)
        print('Player {} sent Hello ack {} to host={}, port={}'.format(self.player, msg, self.host, self.port))

    def wait_for_player(self, first_timeout):
        if self.is_ready:
            prompt = 'Player' + str(self.player)
            self.lbl_player.config(text=prompt)
            if not self._is_my_turn():
                self.wait_for_move()
            return

        if self.player1_turn:
            # player1 is the server
            if not self.is_bound:
                # bind to socket
                self.socket.bind((self.host, self.port))

            try:
                print('waiting... host={}, port={}'.format(self.host, self.port))
                self.is_bound = True
                prompt = 'Waiting...'
                self.lbl_player.config(text=prompt)
                data, addr = self.socket.recvfrom(1024)
                if self.remote is None:
                    self.remote = addr
                msg = data.decode()
                print('received {}'.format(msg))
                parts = msg.split('!')
                msg_type = int(parts[0])
                token = int(parts[2])
                if msg_type == MSG_HELLO and self.token != token:
                    # other player connected to us
                    if self.token < token:
                        self.player = PLAYER1
                    else:
                        self.player = PLAYER2
                    # send acknowledgement
                    self.send_hello_ack()
                    self.is_ready = True
            except socket.timeout as e:
                print('recvfrom timeout: {}'.format(str(e)))
                if first_timeout:
                    self._flip()
                    first_timeout = False
                self.master.update_idletasks()
                self.master.after_idle(self.wait_for_player, first_timeout)
        else:
            self.send_hello()
            try:
                data, addr = self.socket.recvfrom(1024)
                if self.remote is None:
                    self.remote = addr
                msg = data.decode()
                print('received {}'.format(msg))
                parts = msg.split('!')
                msg_type = int(parts[0])
                token = int(parts[2])
                if msg_type == MSG_HELLO_ACK and self.token != token:
                    # the other player was waiting
                    if self.token < token:
                        self.player = PLAYER1
                    else:
                        self.player = PLAYER2
                    self.is_ready = True
                elif msg_type == MSG_HELLO and self.token != token:
                    if self.token < token:
                        self.player = PLAYER1
                    else:
                        self.player = PLAYER2
                    self.send_hello_ack()
                elif self.token == token:
                    # continue sending and waiting
                    self.master.update_idletasks()
                    self.master.after_idle(self.wait_for_player, False)
            except socket.timeout as e:
                print('recvfrom timeout: {}'.format(str(e)))
                # self._flip()
                self.master.update_idletasks()
                self.master.after_idle(self.wait_for_player, False)

    def wait_move_ack(self, w, row, col):
        try:
            data, _ = self.socket.recvfrom(1024)
            msg = data.decode()
            parts = msg.split('!')
            row1, col1 = parts[2].split(',')
            if parts[0] == MSG_MOVE_ACK and self.player != parts[1] and row1 == row and col1 == col:
                print('move {} acknowledged'.format(msg))
                super().process_move(w, row, col)
                # wait for the other player's move
                self.wait_for_move()
        except socket.timeout as e:
            print('wait for move ack timeout: {}'.format(str(e)))
            self.master.update_idletasks()
            self.master.after_idle(self.wait_move_ack, w, row, col)

    def wait_for_move(self):
        try:
            data, _ = self.socket.recvfrom(1024)
            msg = data.decode()
            parts = msg.split('!')
            if parts[0] == MSG_MOVE and self.player != parts[1]:
                print('move {} received'.format(msg))
                row, col = parts[2].split(',')
                w = self._get_widget(row, col)
                super().process_move(w, row, col)
                # acknowledge the other player's move
                self.send_move_ack(row, col)
        except socket.timeout as e:
            print('wait for move timeout: {}'.format(str(e)))
            self.master.update_idletasks()
            self.master.after_idle(self.wait_move_ack, w, row, col)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='127.0.0.1', help="host name for the other player")
    parser.add_argument('--port', default=5005, help="port number for the other player")
    options = parser.parse_args()
    root = Tk()
    grid_image = ImageTk.PhotoImage(Image.open(GRID_FILE))
    game = RemoteGame(root, host=options.host, port=options.port)
    root.mainloop()
