import threading
import time
import random
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s')


def worker():
    logging.debug('starting')
    duration = random.random()
    logging.debug('sleeping for %dms', duration * 1000)
    time.sleep(duration)
    logging.debug('exiting')


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=worker)
        t.setDaemon(True)
        t.start()

    curr_thread = threading.currentThread()
    # map(threading.Thread.join, [t for t in threading.enumerate() if t != curr_thread])
    for t in threading.enumerate():
        if t is not curr_thread:
            logging.debug('waiting for thread %s to terminate', t.name)
            t.join(10)