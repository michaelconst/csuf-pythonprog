import threading
import random


class Die:
    def __init__(self):
        self._throw()

    def __str__(self):
        return str(self.n)

    def _throw(self):
        self.n = random.randint(1, 6)

    def __call__(self, *args, **kwargs):
        self._throw()

    @staticmethod
    def over(threshold, dice):
        return dice[0].n + dice[1].n >= threshold


def throw(index, threshold):
    dice = (Die(), Die())
    print('[{}] ({},{}){}'.format(index, *dice, ' you won!' if Die.over(threshold, dice) else ''))


def main(threshold):
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=throw, args=(i, threshold)))

    for t in threads:
        t.start()


if __name__ == '__main__':
    import sys
    import os

    if len(sys.argv) < 2:
        print('usage {} <wining-threshold>'.format(os.path.basename(__file__)))
        sys.exit(1)

    main(int(sys.argv[1]))