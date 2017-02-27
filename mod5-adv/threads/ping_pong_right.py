from threading import Thread, Condition, Lock
import time
import random


class Player(Thread):
    turn = 'player1'

    def __init__(self, first_condition, second_condition, score, first=True, history=None):
        super().__init__()
        self.name = 'player1' if first else 'player2'
        self.play_msg = 'ping' if first else 'pong'
        self.index = 0 if first else 1
        self.first_condition = first_condition
        self.second_condition = second_condition
        self.score = score
        self.history = history

    def play(self):
        print('[{}] {}'.format(self.name, self.play_msg))
        time.sleep(0.01)
        if self.history is not None:
            self.history.append(self.play_msg)
        r = random.random()
        if r < 0.35:
            # lost the exchange
            self.score.update(self.index, win=False)

    def run(self):
        while True:
            if self.score.game_over():
                return

            with self.first_condition:
                while not Player.turn == self.name:
                    self.first_condition.wait()

            self.play()

            with self.first_condition:
                Player.turn = 'player1' if Player.turn == 'player2' else 'player2'
                self.second_condition.notify()


class Score:
    def __init__(self, max_score=10):
        self.max_score = max_score
        self.score = [0, 0]

    def update(self, index, win=True):
        assert index in (0, 1)
        if self.game_over():
            return
        if win:
            self.score[index] += 1
        else:
            self.score[1 - index] += 1
        print('{}-{}'.format(self.score[0], self.score[1]))

    def won(self):
        """
        return 0 if first player won, 1 if second player won and -1 if game is not over yet
        :return: 0, 1 or -1
        """
        if not self.game_over():
            return -1
        for i, points in enumerate(self.score):
            if points == self.max_score:
                return i

    def game_over(self):
        return any([True for x in self.score if x == self.max_score])


def main():
    score = Score(max_score=21)
    history = []
    lock = Lock()
    c1 = Condition(lock)
    c2 = Condition(lock)
    player1 = Player(c1, c2, score, history=history)
    player1.start()
    player2 = Player(c2, c1, score, first=False, history=history)
    player2.start()
    player1.join()
    player2.join()

    result = score.won()
    if result == -1:
        # something went wrong
        print('threads terminated before the game was over!')

    wining_player = 'player' + str(result+1)
    print('game over! {} won'.format(wining_player))

    # check if 2 consecutive plays are the same
    if history is not None:
        print('number of plays: %d' % len(history))
        history_pairs = list(zip(history, history[1:]))
        for i, (p1, p2) in enumerate(history_pairs):
            if p1 == p2:
                print('play error at {}'.format(i))
        assert not any([True for x, y in history_pairs if x == y])


if __name__ == '__main__':
    main()