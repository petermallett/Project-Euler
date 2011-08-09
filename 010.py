#Find the sum of all the primes below two million.
import math
import time

from projecteuler import sieve

start = time.clock()

p = sieve(2000000)
sum = 0
for x in p:
	sum += x

print(sum)

print('Elapsed time:', time.clock() - start)

