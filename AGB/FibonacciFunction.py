# FaaS to deployed in Google Cloud Run.

import timeit


def fib_doubling(n):
    if (n < 2) or (n > 100000001):
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


if __name__ == "__main__":

    # Tests parameters
#    print("fib_doubling             -2 :\t",
#          timeit.timeit('fib_doubling(-2)', globals=globals(), number=1))
#    print("fib_doubling  1 000 000 001 :\t", timeit.timeit(
#        'fib_doubling(1000000001)', globals=globals(), number=1))

    # Compute parameters
    print("fib_doubling              20 :\t", timeit.timeit(
        'fib_doubling(20)', globals=globals(), number=1))
    print("fib_doubling             200 :\t", timeit.timeit(
       'fib_doubling(200)', globals=globals(), number=1))
 #   print("fib_doubling            100 :\t", timeit.timeit(
 #       'fib_doubling(100)', globals=globals(), number=1))
 #   print("fib_doubling          1 000 :\t", timeit.timeit(
 #       'fib_doubling(1000)', globals=globals(), number=1))
 #   print("fib_doubling         10 000 :\t", timeit.timeit(
 #       'fib_doubling(10000)', globals=globals(), number=1))
 #   print("fib_doubling        100 000 :\t", timeit.timeit(
 #       'fib_doubling(100000)', globals=globals(), number=1))
 #   print("fib_doubling      1 000 000 :\t", timeit.timeit(
 #       'fib_doubling(1000000)', globals=globals(), number=1))
 #   print("fib_doubling     10 000 000 :\t", timeit.timeit(
 #       'fib_doubling(10000000)', globals=globals(), number=1))
 #   print("fib_doubling     50 000 000 :\t", timeit.timeit(
 #       'fib_doubling(50000000)', globals=globals(), number=1))
    print("fib_doubling    100 000 000 :\t", timeit.timeit(
        'fib_doubling(100000000)', globals=globals(), number=1))
