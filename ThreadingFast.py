from threading import *


class Demo:
    def num(self):
        for i in range(1, 100000):
            print("The number is ", i)

    def double(self):
        for i in range(1, 100000):
            print("The double of the number is ", 2 * i)

    def square(self):
        for i in range(1, 100000):
            print("The square of the number is ", i * i)


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
