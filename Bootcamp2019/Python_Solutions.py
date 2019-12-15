# Practice!

# Question 1
# Can you write a short program that will print out the version of Python
# that you are using?

import sys

py_version = sys.version
print('You are using version',py_version)


# Question 2
# Write a program that requests five names separated by commas and create a
# list containing those names. Print your answer.
# For example James,Alison,Fred,Sally,Matthew
# should return ['James','Alison','Fred','Sally','Matthew']

names = input('Please enter names separated by commas: ')
name_list = names.split(',')
print(name_list)


# Question 3
# Write a program to determine whether a given number is within 10 of 100 or 200.

def(number):
    if (abs(100 - number)) <= 10 or (abs(200 - number)) <= 10:
        return True
    else:
        return False


# Question 4
# Write a program that takes a list of non-negative integers and prints each integer
# to the screen the same number of times as the value of the integer, each new value
# on a new line. For example
# [2,3,4,1] would print:
# 22
# 333
# 4444
# 1

def print_nums(number_list):

    for item in number_list:
        while item > 0:
            value = str(item) * item
            print(value)


# Question 5
# Write some code that will return the number of CPUs in the system.

import multiprocessing
print(multiprocessing.cpu_count())


# Question 6
# Write a program that will return the sum of the digits of an integer.

def digit_sum(number):
    sum = 0
    while number > 0:
        sum = sum + number % 10
        number = number // 10
    return sum


# Question 7
# Write a program that converts text into pig latin. Pig latin works as follows:
# All letters before initial vowel are placed at the end of the word and then 'ay'
# is added (explanation adapted from Wikipedia), so pig becomes igpay, cat becomes
# atcay, potential becomes otentialpay etc.

def pig_latin(word):
    vowels = ['a','e','i','o','u']
    front = None
    for index, char in enumerate(word):
        if char in vowels:
            front = word[index:]
            back = word[:index]
            break
    if not front:
        return 'No vowels!'
    translation = front + back + 'ay'
    return translation


# Question 8
# Write a function that will check for the occurrence of double letters in
# a string. If the string contains double letters next to each other it
# will return True, otherwise it will return False.

def double(string):
    str_len = len(string)
    for i in range(str_len - 1):
        if string[i] == string[i+1]:
            return True

    return False


# Question 9
# Write a function that will check if a string is a palindrome.

def palindrome(string):
    if string == string[::-1]:
        return True
    return False


# Question 10
# Write a function def add_commas(numbers) that will add commas to an integer and return it as a string.
# For example add_commas(1000000) will return 1,000,000 Do it first without using string fomratting
# or f strings.

def add_commas(number):

    str_number = str(number)

    str_number = str_number[::-1]
    comma = ','
    new_str = ''
    for i, num in enumerate(str_number):
        if i != 0 and (i % 3) == 0:
            new_str = new_str + comma
        new_str = new_str + num

    return new_str[::-1]


# Question 11
# Write a function that will convert an integer into binary.

def to_binary(number):
    print(f'{number} in binary is {number:08b})


# Question 12
# Write a function that calculates the sum of all integers up to n. Use the iterative method
# and the formula and compare the results. (sum of n integers given by S = (n(n+1))/2)

def check_sums(number):
    sum_1 = 0
    for i,v in enumerate(range(number+1)):
        sum_1 = sum_1 + v
    sum_2 = (number * (number + 1))/2

    return sum_1, sum_2


# Question 13
# Go back over the TwoSum problem we covered earlier in the course. Ensure you understand it.


# Question 14
# Implement the TwoSum solution without referring to the solution.


# Question 15
# Write a function that takes a positive integer n and converts it into hours and minutes.
# 45 would return 0h:45mins 135 would return 2h:15mins

def convert_h_m(num):
  hours = num // 60
  mins = num % 60
  return str(hours) + 'h' + ':' + str(mins)  + ' mins'


# Question 16
# Write a function to determine whether all numbers in a list are unique.

def unique_items(my_list):
    if len(my_list) == len(set(my_list)):
        return True
    else:
        return False


# Question 17
# Write a function to add two positive integers together without using the + operator.
# (Note, this will require some research - start here https://en.wikipedia.org/wiki/Bitwise_operation)

def no_plus_sum(a,b):

    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a
# Explanation: https://stackoverflow.com/questions/17342042/why-this-code-for-additionusing-bitwise-operation-works-in-java


 # Question 18
# Write a function that will calculate the number of divisors of a positive integer and return
# those divisors.

def num_divisors(num):
    divisors = [i for i in range(1,num + 1) if num%i ==0]
    return (divisors, len(divisors))


# Question 19
# Write a function that uses bitwise operations to determine whether a number is odd or even.

def odd_even(num):
    if (num & 1):
        print('Odd')
    print('Even')


 # Question 20
# Write a function which prints the prime numbers in a given range.

def primes(start,end):
    primes = []
    for i in range(start,end+1):
        if i>1:
            for j in range(2,i):
                if i%j == 0:
                    break

            else:
                primes.append(i)
      return primes
      #(Note the use of the for/else clause here - it can be extremely useful - https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops)   
