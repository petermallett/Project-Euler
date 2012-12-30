# What is the 10001st prime number?

import math

def is_prime(n):
    if (n < 2):
        return False

    for x in range(2, int(math.sqrt(n))+1):
        if (n % x == 0):
            return False

    return True

def find_next_prime(n):
    while(True):
        n += 2
        if (is_prime(n)):
            return n

#starting with 2nd prime
number = 2
prime = 3
while (number != 10001):
    prime = find_next_prime(prime)
    number += 1

print(prime)
