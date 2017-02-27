from multiprocessing import Process, Queue

def power2(q):
    nums = q.get()
    squares = [x * x for x in nums]
    q.put(squares)

if __name__ == '__main__':
    q = Queue()
    p = Process(target=power2, args=(q,))
    p.start()
    q.put([3, 5, 7])
    p.join()
    print('squares; {}'.format(q.get()))