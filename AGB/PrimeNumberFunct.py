# Analysis of Different Methods to find Prime Number in Python
# Ref : https://www.geeksforgeeks.org/analysis-different-methods-find-prime-number-python/
import math
import time


def is_prime_for(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_sqrt(n):
    if n <= 1:
        return False
    max_div = math.floor(math.sqrt(n))
    for i in range(2, 1 + max_div):
        if n % i == 0:
            return False
    return True


def is_prime_opt(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True


# Driver for is_prime_for()
t0 = time.time()
c = 0  # for counting
for n in range(1, 100000):
    x = is_prime_for(n)
    c += x
print("is_prime_for(n) / Total prime numbers in range \t:\t", c)
t1 = time.time()
print("Time required :", t1 - t0)

# Driver for is_prime_sqrt()
t0 = time.time()
c = 0  # for counting
for n in range(1, 100000):
    x = is_prime_sqrt(n)
    c += x
print("is_prime_sqrt(n) / Total prime numbers in range \t:\t", c)
t1 = time.time()
print("Time required :", t1 - t0)

# Driver for is_prime_opt()
t0 = time.time()
c = 0  # for counting
for n in range(1, 100000):
    x = is_prime_opt(n)
    c += x
print("is_prime_opt(n) / Total prime numbers in range \t:\t", c)
t1 = time.time()
print("Time required :", t1 - t0)
