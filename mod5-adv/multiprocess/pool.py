import multiprocessing


def power2(n):
    return n * n


def power3(n):
    return n * n * n


def init_process():
    print('Starting', multiprocessing.current_process().name)


if __name__ == '__main__':
    # create a pool with default number of processes (# of CPU cores)
    pool = multiprocessing.Pool(initializer=init_process, maxtasksperchild=2)
    # same as the built-in map, but executed in parallel
    results2 = pool.map(power2, range(1, 10))
    results3 = pool.map_async(power3, range(1, 10))
    ar = pool.map_async(power2, range(1, 5), callback=lambda res: print('async callback result: %s' % res))
    # close the pool, no more tasks allowed
    pool.close()
    print('results: {}'.format(results2))
    print('results: {}'.format(results3.get()))
    ar.wait()