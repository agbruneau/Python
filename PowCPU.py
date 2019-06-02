# Ref : https://weeraman.com/put-that-gpu-to-good-use-with-python-e5a437168c01

from timeit import default_timer as timer
import numpy as np


def pow(a, b, c):
    for i in range(a.size):
        c[i] = a[i] ** b[i]


def main():
    vec_size = 100000000

    a = b = np.array(np.random.sample(vec_size), dtype=np.float32)
    c = np.zeros(vec_size, dtype=np.float32)

    start = timer()
    pow(a, b, c)
    duration = timer() - start

    print(duration)


if __name__ == '__main__':
    main()
