#find the largest prime factor of 600851475143
import math

from projecteuler import find_prime_factors

number = 600851475143

pf = find_prime_factors(number)

print(pf[-1])

