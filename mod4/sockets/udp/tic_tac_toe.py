from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import Separator


X_FILE = 'images/x.png'
O_FILE = 'images/o.png'
# use a grid image
GRID_FILE = 'images/grid.png'


class Game:
    def __init__(self, master, player1=True, player1_img=X_FILE, player2_img=O_FILE):
        self.master = master
        self.frame = Frame(self.master, padx=10, pady=10, background='black')
        self.frame.pack()
        image1 = ImageTk.PhotoImage(Image.open(player1_img))
        image2 = ImageTk.PhotoImage(Image.open(player2_img))
        self.player1_img = image1
        self.player2_img = image2
        self.cell_size = max(image1.width(), image1.height(), image2.width(), image2.height()) + 1
        self.player1_turn = player1
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.player = Label(self.frame, text="Player1", font="Arial 20 bold",
                            borderwidth=5, highlightbackground="red", background="black", foreground='white')
        self.player.grid(columnspan=3, sticky=W)
        # import random
        # r = lambda: random.randint(0, 255)
        # self.colors = [['#%02X%02X%02X' % (r(), r(), r()) for i in range(3)] for j in range(3)]

        for i in range(1, 6, 2):
            for j in range(0, 5, 2):
                name = "lbl-%d%d" % ((i-1)/2+1, j/2+1)
                inner_frame = Frame(self.frame, name=name, width=self.cell_size, height=self.cell_size)
                inner_frame.pack_propagate(0)
                inner_frame.grid(row=i, column=j, sticky=E+W+N+S, padx=2, pady=2)
                inner_frame.bind('<Button-1>', self.on_click)

        for i in range(2, 5, 2):
            Separator(self.frame, orient=HORIZONTAL).grid(row=i, columnspan=5, column=0, sticky=EW)
            for j in range(1, 4, 2):
                Separator(self.frame, orient=VERTICAL).grid(row=1, rowspan=5, column=j, sticky=NS)
                self.frame.grid_columnconfigure(j, weight=3)

    def on_click(self, event):
        w = event.widget
        print('clicked on label {}'.format(w))
        index = w.winfo_name()[4:]
        x = int(index[0]) - 1
        y = int(index[1]) - 1
        self.process_move(w, x, y)

    def process_move(self, w, row, col):
        if self.board[row][col] == 0:
            if self.player1_turn:
                img = self.player1_img
                prompt = "Player2"
                val = 1
            else:
                img = self.player2_img
                prompt = "Player1"
                val = 2
            self.board[row][col] = val
            lbl = Label(w, image=img)
            lbl.pack(fill=BOTH, expand=1)
            self.player.config(text=prompt)
            self.player1_turn = not self.player1_turn

            winner = self.get_winner(self.board)
            prompt = None
            if winner and winner == 1:
                prompt = "Player1 won!"
            elif winner and winner == 2:
                prompt = "Player2 won!"
            if prompt:
                self.player.config(text=prompt)

    def get_winner(self, board):
        winner = Game._get_row_winner(board)
        if winner:
            return winner
        transpose = [[row[j] for row in board] for j in range(3)]
        winner = Game._get_row_winner(transpose)
        if winner:
            return winner
        diag1 = [board[i][i] for i in range(3)]
        diag2 = [board[i][2-i] for i in range(3)]
        winner = Game._get_row_winner([diag1, diag2])
        if winner:
            return winner
        # check how many empty squares left
        empty, pos = Game._get_empty(board)
        if empty == 0:
            self.player.config(text="Draw!")
        elif empty == 1 and pos:
            import copy
            board2 = copy.deepcopy(board)
            board2[pos[0]][pos[1]] = 1
            if Game.get_winner(board2):
                return
            board2 = copy.deepcopy(board)
            board2[pos[0]][pos[1]] = 2
            if Game.get_winner(board2):
                return
            self.player.config(text="Draw!")

    @staticmethod
    def _get_row_winner(board):
        player1 = [all(v == 1 for v in row) for row in board]
        if any(player1):
            return 1
        player2 = [all(v == 2 for v in row) for row in board]
        if any(player2):
            return 2

    @staticmethod
    def _get_empty(board):
        count = 0
        pos = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    count += 1
                    if count > 1:
                        return count, None
                    if pos is None:
                        pos = (i, j)
        return count, pos


if __name__ == '__main__':
    root = Tk()
    grid_image = ImageTk.PhotoImage(Image.open(GRID_FILE))
    game = Game(root)
    mainloop()
