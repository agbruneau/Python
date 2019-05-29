# Futur Fonction en CaaS dans Google Cloud Run à ajouter et expérimenter.
import timeit

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

    print("fib_doub        200 :\t", timeit.timeit('fib_doubling(200)', globals=globals(), number=1))
    print("fib_doub      2 000 :\t", timeit.timeit('fib_doubling(2000)', globals=globals(), number=1))
    print("fib_doub     20 000 :\t", timeit.timeit('fib_doubling(20000)', globals=globals(), number=1))
    print("fib_doub    200 000 :\t", timeit.timeit('fib_doubling(200000)', globals=globals(), number=1))
    print("fib_doub  2 000 000 :\t", timeit.timeit('fib_doubling(2000000)', globals=globals(), number=1))
    print("fib_doub 20 000 000 :\t", timeit.timeit('fib_doubling(20000000)', globals=globals(), number=1))
