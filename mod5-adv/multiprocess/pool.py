import multiprocessing

def calculate(n):
    return n * n

def init_process():
    print('Starting', multiprocessing.current_process().name)

if __name__ == '__main__':
    # create a pool with default number of processes (# of CPU cores)
    pool = multiprocessing.Pool(initializer=init_process, maxtasksperchild=2)
    # same as the built-in map, but executed in parallel
    results = pool.map(calculate, range(1, 10))
    # close the pool, no more tasks allowed
    pool.close()
    # wait for all processes to complete their tasks
    pool.join()
    print('results: {}'.format(results))