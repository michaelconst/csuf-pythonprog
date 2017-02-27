import threading
import time
from collections import Counter
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s')
counter = 0
processed_items = Counter()
lock = threading.Lock()

def visit():
    global counter
    for i in range(10):
        # processing item
        with lock:
            logging.debug('processing item %d', counter)
            processed_items[counter] += 1
            time.sleep(0.001)
            counter += 1


for i in range(5):
    threading.Thread(target=visit).start()

for thread in threading.enumerate():
    if thread is not threading.current_thread():
        thread.join()

print('counter=%d' % counter)
total_processings = 10 * 5
assert counter == total_processings, 'counter should have been %d' % total_processings
for item, count in processed_items.items():
    if count != 1:
        print('item {} was processed {} times'.format(item, count))