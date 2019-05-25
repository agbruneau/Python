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
obj.num()
obj.double()
obj.square()

print("This is the main Thread")
