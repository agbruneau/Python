import time
from threading import *


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


if __name__ == "__main__":
    t0 = time.time()

    obj = Demo()
    t1 = Thread(target=obj.num)
    t2 = Thread(target=obj.double)
    t3 = Thread(target=obj.square)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("This is the main Thread")

    t1 = time.time()
    print("Time required :", t1 - t0)
