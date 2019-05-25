# Prime Numbers using Python
# Ref : https://hackernoon.com/prime-numbers-using-python-824ff4b3ea19
import timeit


def approach1(given_number):
    # Initialize a list
    primes = []
    for possible_prime in range(2, given_number + 1):
        # Assume number is prime until shown it is not.
        is_prime = True
        for num in range(2, possible_prime):
            if possible_prime % num == 0:
                is_prime = False
        if is_prime:
            primes.append(possible_prime)
    return primes


def approach2(given_number):
    # Initialize a list
    primes = []
    for possible_prime in range(2, given_number + 1):
        # Assume number is prime until shown it is not.
        is_prime = True
        for num in range(2, possible_prime):
            if possible_prime % num == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(possible_prime)
    return primes


def approach3(given_number):
    # Initialize a list
    primes = []
    for possible_prime in range(2, given_number + 1):
        # Assume number is prime until shown it is not.
        is_prime = True
        for num in range(2, int(possible_prime ** 0.5) + 1):
            if possible_prime % num == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(possible_prime)
    return primes


# Approach 1: Execution time
print(timeit.timeit('approach1(500)', globals=globals(), number=1000))
# Approach 2: Execution time
print(timeit.timeit('approach2(500)', globals=globals(), number=1000))
# Approach 3: Execution time
print(timeit.timeit('approach3(500)', globals=globals(), number=1000))
