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

    def pow4(self):
        for i in range(1, 100000000):
            z = i * i * i * i

    def pow(self):
        vec_size = 100000000
        a = b = np.array(np.random.sample(vec_size), dtype=np.float)
        c = np.zeros(vec_size, dtype=np.float)
        for i in range(a.size):
            c[i] = a[i] ** b[i]


if __name__ == "__main__":
    start = timer()

    obj = Demo()
    t1 = Thread(target=obj.num)
    t2 = Thread(target=obj.double)
    t3 = Thread(target=obj.square)
    t4 = Thread(target=obj.pow4)
    t5 = Thread(target=obj.pow)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    print("Thread t1 Num running time : ", timer() - start)

    t2.join()
    print("Thread t2 Double running time : ", timer() - start)

    t3.join()
    print("Thread t3 Square running time : ", timer() - start)

    t4.join()
    print("Thread t4 Pow4 running time : ", timer() - start)

    t5.join()
    print("Main Thread t5 Pow running time : ", timer() - start)
