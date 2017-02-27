import threading
import time
import random
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')


class MyThread(threading.Thread):
    def __init__(self, timeout):
        super().__init__()
        self.timeout = timeout

    def run(self):
        logging.debug('sleeping {}s'.format(self.timeout))
        time.sleep(self.timeout)
        logging.debug('exiting')


for i in range(5):
    MyThread(random.randint(1, 5)).start()