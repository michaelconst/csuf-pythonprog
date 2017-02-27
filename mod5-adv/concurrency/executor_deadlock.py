from concurrent.futures import ThreadPoolExecutor
import time


def p1():
    time.sleep(5)
    print(r2.result())  # b will never complete because it is waiting on a.
    return 1


def p2():
    time.sleep(5)
    print(r1.result())  # a will never complete because it is waiting on b.
    return 2


executor = ThreadPoolExecutor(max_workers=2)
r1 = executor.submit(p1)
r2 = executor.submit(p2)