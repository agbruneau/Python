# Ref : https://www.geeksforgeeks.org/python-plotting-fibonacci-spiral-fractal-using-turtle/
# Python program for Plotting Fibonacci
# spiral fractal using Turtle
import math
import turtle


def fib_plot(n):
    a = 0
    b = 1
    square_a = a
    square_b = b

    # Setting the colour of the plotting pen to blue
    x.pencolor("blue")

    # Drawing the first square
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)

    # Proceeding in the Fibonacci Series
    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    # Drawing the rest of the squares
    for i in range(1, n):
        x.backward(square_a * factor)
        x.right(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)

        # Proceeding in the Fibonacci Series
        temp = square_b
        square_b = square_b + square_a
        square_a = temp

    # Bringing the pen to starting point of the spiral plot
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()

    # Setting the colour of the plotting pen to red
    x.pencolor("red")

    # Fibonacci Spiral Plot
    x.left(90)
    for i in range(n):
        print(b)
        fdwd = math.pi * b * factor / 2
        fdwd /= 90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        temp = a
        a = b
        b = temp + b


if __name__ == "__main__":
    # factor which expands or shrinks the scale of the plot by a certain factor.
    factor = 1

    # Iterations our Algorithm will run
    nbre = 12

    # Plotting the Fibonacci Spiral Fractal and printing the corresponding Fibonacci Number
    print("Fibonacci series for", nbre, "elements :")
    x = turtle.Turtle()
    x.speed(100)
    fib_plot(nbre)
    turtle.done()
