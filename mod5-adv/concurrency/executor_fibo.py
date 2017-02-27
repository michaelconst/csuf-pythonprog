import concurrent.futures
import functools

NUMBERS = [20, 40, 60, 80, 100]


@functools.lru_cache()
def fibo(n):
    """Recursive function to
   print Fibonacci sequence"""
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for n, fibo_num in zip(NUMBERS, executor.map(fibo, NUMBERS)):
            print('Fibonacci({}) = {}'.format(n, fibo_num))


if __name__ == '__main__':
    main()
