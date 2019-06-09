import numpy as np
from threading import *
from timeit import default_timer as timer


class Demo:
    def num(self):
        for i in range(1, 100000000):
            x = i

    def double(self):
        for i in range(1, 100000000):
            y = 2 * i

    def square(self):
        for i in range(1, 100000000):
            z = i * i

    def pow(self):
        vec_size = 100000000
        a = b = np.array(np.random.sample(vec_size), dtype=np.float32)
        c = np.zeros(vec_size, dtype=np.float32)
        for i in range(a.size):
            c[i] = a[i] ** b[i]


if __name__ == "__main__":
    start = timer()

    obj = Demo()
    t1 = Thread(target=obj.num)
    t2 = Thread(target=obj.double)
    t3 = Thread(target=obj.square)
    t4 = Thread(target=obj.pow)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("This is the main Thread")
    print(timer() - start)
