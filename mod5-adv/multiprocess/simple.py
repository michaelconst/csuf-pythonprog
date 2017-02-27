import multiprocessing
import time
import random
import os


def do_work(t):
    pid = 'unknown'
    if hasattr(os, 'getpid'):
        pid = os.getpid()
    print('[{} {} {}] sleeping {}s'.format(pid, __name__, time.time(), t))
    time.sleep(t)
    print('[{} {} {}] exiting'.format(pid, __name__, time.time()))


def main():
    processes = []
    for i in range(5):
        processes.append(multiprocessing.Process(target=do_work, args=(random.randint(1, 5),)))
    for p in processes:
        p.start()
    for p in processes:
        p.join()


if __name__ == '__main__':
    main()

