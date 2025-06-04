# import numpy as np
import math # Allows math.log(value,base)

# add_numbers calculates the sum of two numbers
def add_numbers(num1, num2):
    return num1 + num2

# test_prime_number is a Boolean function.
# True if a given integer is a prime number. Otherwise, it returns False.
def test_prime_number(num):
    if num in range(2):
        return False
    for i in range(2, num+1):
        if i == num: # num is a prime number if no lower number was a divisor of num
            return True
        if num % i == 0: # test if divisible by i
            return False

# Calculate a list of all prime numbers up to a given integer
# (Inefficient algorithm: works up to around 100 000 in medium time)
# Better: Sieb des Eratosthenes directly at the start
def list_prime_numbers(num):
    prime_numbers = list()
    for i in range(num):
        if test_prime_number(i):
            prime_numbers.append(i)
    return prime_numbers

# Calculate the number of prime numbers up to a given integer
def number_prime_numbers(num):
    return len(list_prime_numbers(num))

a = list_prime_numbers(100)
b = number_prime_numbers(100)
#print(a)
#print(b)

x = math.log(20, 3)
print(x)

y = math.degrees(math.asin(0.6))
print(math.asin(0.6))
print("Winkel:", y)

z = math.cos(math.radians(30))
print("z", z)
