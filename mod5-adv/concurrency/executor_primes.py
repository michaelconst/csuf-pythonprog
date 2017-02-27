import concurrent.futures
import math
import functools


@functools.lru_cache()
def fibo(n):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
    #         print('%d is prime: %s' % (number, prime))
    fn = fibo(100)
    print('Fibonacci number for 10 = {}'.format(fn))

if __name__ == '__main__':
    main()