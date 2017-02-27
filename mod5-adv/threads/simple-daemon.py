import threading
import time
import random

def do_work(t):
    print('[{}] sleeping {}s'.format(threading.current_thread().name, t))
    time.sleep(t)
    print('[{}] exiting'.format(threading.current_thread().name))

for i in range(5):
    thread = threading.Thread(target=do_work, args=(random.randint(1, 5),))
    thread.daemon = True
    thread.start()

for thread in threading.enumerate():
    thread.join(5.1)