def fibbonaci(n):
    if n < 2:
        return n

    a, b = 0, 1

    for i in range(1, n):
        a, b = b, a + b
    return b


# Main Python 
if __name__ == "__main__":
    print(fibbonaci(100))
