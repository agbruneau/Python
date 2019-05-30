# Futur Fonction en CaaS dans Google Cloud Run à ajouter et expérimenter.
import timeit

def fib_doubling(n):
    if (n < 2) or (n > 100000000):
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

    # Tests parameters limites
    print("fib_doub             -2 :\t",timeit.timeit('fib_doubling(-2)', globals=globals(), number=1))
    print("fib_doub  1 000 000 001 :\t", timeit.timeit('fib_doubling(1000000001)', globals=globals(), number=1))

    # Compute parameters
    print("fib_doub              1 :\t", timeit.timeit('fib_doubling(1)', globals=globals(), number=1))
    print("fib_doub             10 :\t", timeit.timeit('fib_doubling(10)', globals=globals(), number=1))
    print("fib_doub            100 :\t", timeit.timeit('fib_doubling(100)', globals=globals(), number=1))
    print("fib_doub          1 000 :\t", timeit.timeit('fib_doubling(1000)', globals=globals(), number=1))
    print("fib_doub         10 000 :\t", timeit.timeit('fib_doubling(10000)', globals=globals(), number=1))
    print("fib_doub        100 000 :\t", timeit.timeit('fib_doubling(100000)', globals=globals(), number=1))
    print("fib_doub      1 000 000 :\t", timeit.timeit('fib_doubling(1000000)', globals=globals(), number=1))
    print("fib_doub     10 000 000 :\t", timeit.timeit('fib_doubling(10000000)', globals=globals(), number=1))
 #   print("fib_doub    100 000 000 :\t", timeit.timeit('fib_doubling(100000000)', globals=globals(), number=1))
 #   print("fib_doub  1 000 000 000 :\t", timeit.timeit('fib_doubling(1000000000)', globals=globals(), number=1))
