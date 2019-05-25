# Futur Fonction en CaaS dans Google Cloud Run à ajouter et expérimenter.
import time

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

    start_time = time.time()
    fib_doubling(20000000)
    print("Time Running for Fib_Doubling of 20 millions : %.9fs" % (time.time() - start_time))
