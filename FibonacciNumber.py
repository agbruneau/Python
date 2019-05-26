# Fibonacci Web Calculator - Max : 20000
# http://php.bubble.ro/fibonacci/

import time
from functools import lru_cache
from functools import reduce


class Fibonacci:

    def __init__(self, max=12600000000):
        self.a, self.b = 0, 1
        self.max = max

    def __iter__(self):
        # Return the iterable object (self)
        return self

    def next(self):
        # When we need to stop the iteration we just need to raise
        # a StopIteration exception
        if self.a > self.max:
            raise StopIteration

        # save the value that has to be returned
        value_to_be_returned = self.a

        # calculate the next values of the sequence
        self.a, self.b = self.b, self.a + self.b

        return value_to_be_returned

    def __next__(self):
        # For compatibility with Python3
        return self.next()


# Fib Recursive with lru_cache implementing a Native Dynamic Programming Technique
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# Dynamic programming »
# https://avikdas.com/2019/04/15/a-graphical-introduction-to-dynamic-programming.html?utm_medium=email&utm_source=topic+optin&utm_campaign=awareness&utm_content=20190420+prog+nl&mkt_tok=eyJpIjoiTmpJeE1USTROVEF5TVRJeCIsInQiOiJSOTZ0MlExYXk1V0tqNk9nQUN0anhYc3BIZjVwbkw3RktXdXhxeUhFNE5lWWpHWFVxeU9MMyt6dVpyMU5vXC9tMURCNVhtNFlCT3l3a2xKb1VrNTJjSEY3MGQ1b2ZoNndBTXpzKzVXakk3UFpISnp3TGFVZUZsaytYczlnVW5KT28ifQ%3D%3D
def fib_cache(n, cache=None):
    if n < 2:
        return n
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]

    result = fib_cache(n - 1, cache) + fib_cache(n - 2, cache)
    cache[n] = result
    return result


# Different implementation of Fib functions
def fib_fast(n):
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(1, n + 1):
        a, b = b, a + b
    return b


def fib_house_robber(house_values):
    if house_values < 2:
        return house_values
    a, b = 0, 1
    for val in house_values:
        a, b = b, max(b, a + val)
    return b


def fib_reduce(n):
    if n < 2:
        return n
    return reduce(lambda x, n: [x[1], x[0] + x[1]], range(n), [0, 1])[0]


def fib_ia(n):
    if n < 2:
        return n
    return pow(2 << n, n + 1, (4 << 2 * n) - (2 << n) - 1) % (2 << n)


def fib_doubling(n):
    if n < 2:
        return n
    """ Calculate the Nth Fibonacci number using the doubling method. """
    return _fib_doubling(n)[0]


def _fib_doubling(n):
    """ Calculate Nth Fibonacci number using the doubling method. Return the
    tuple (F(n), F(n+1))."""
    if n == 0:
        return 0, 1
    else:
        a, b = _fib_doubling(n >> 1)
        c = a * ((b << 1) - a)
        d = a * a + b * b
        if n & 1:
            return d, c + d
        else:
            return c, d

# Main Python 
if __name__ == "__main__":

    print("Fib Native Dynamic Programming Technique")
    # fib Native with LRU Cache
    start_time = time.time()
    fib(499)
    print("fib 499 lru  \t\t: %.9fs" % (time.time() - start_time))

    # Fib Native with Cache
    start_time = time.time()
    fib_cache(499, None)
    print("fib_cache 499 \t\t: %.9fs" % (time.time() - start_time))

    # Using Optimized Fibonacci Functions.
    fib_num = 20000

    print()
    print("fib of 2 000 with number of decimals :", len(str(fib_doubling(fib_num))))

    start_time = time.time()
    fib_fast(fib_num)
    print("fib_fast \t\t: %.9fs" % (time.time() - start_time))

    start_time = time.time()
    fib_reduce(fib_num)
    print("fib_reduce \t\t: %.9fs" % (time.time() - start_time))

    start_time = time.time()
    fib_ia(fib_num)
    print("fib_ia \t\t\t: %.9fs" % (time.time() - start_time))

    start_time = time.time()
    fib_doubling(fib_num)
    print("fib_doubling \t: %.9fs" % (time.time() - start_time))

    print()
    start_time = time.time()
    fib_doubling(20000000)
    print("fib_doubling 20 millions : %.9fs" % (time.time() - start_time))

    print()
    print("Fibonacci Doubling 50")
    start_time = time.time()
    for x in range(0, 50):
        print(x, fib_doubling(x))
    print("Fibonacci Doubling 50 time : %.9fs" % (time.time() - start_time))

    # Commentaire de test GitHub pour la classe Fibonacci
    print()
    print("Fibonacci Class 50")
    MY_FIBONACCI_NUMBERS = Fibonacci()
    x = 0
    start_time = time.time()
    for fibonacci_number in MY_FIBONACCI_NUMBERS:
        print(x, fibonacci_number)
        x = x + 1
    print("Fibonacci Class 50 time : %.9fs" % (time.time() - start_time))
