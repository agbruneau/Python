class Demo:
    def __init__(self):
        pass

    def __iter__(self):
        return self

    def num(self):
        for i in range(1, 1000):
            print("The number is ", i)

    def double(self):
        for i in range(1, 1000):
            print("The double of the number is ", 2 * i)

    def square(self):
        for i in range(1, 1000):
            print("The square of the number is ", i * i)


obj = Demo()
obj.num()
obj.double()
obj.square()
