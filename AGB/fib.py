import timeit


def fibbonaci(n):
    if n < 2:
        return n

    a, b = 0, 1

    for i in range(1, n):
        a, b = b, a + b
    return b


# Main Python 
if __name__ == "__main__":
    print("fib_doubling    1 000 000 :\t", timeit.timeit(
       'fibbonaci(1000000)', globals=globals(), number=1))
