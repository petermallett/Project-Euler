#What is the value of the first triangle number to have over five hundred divisors?

from projecteuler import find_prime_factors

###
# Generates a powerset.
def powerset(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

###
# Returns the product of all elements of a set.
def set_product(seq):
    if len(seq) == 1:
        return seq[0]
    else:
        prod = 1
        for x in seq:
            prod *= x
        return prod

###
# Creates a set of all the factors by computing all the possible products of
# the prime factors and returns the count.
def count_factors(n):
    prime_factors = find_prime_factors(n)
    factors = set(prime_factors)
    new_factors = [set_product(x) for x in powerset(prime_factors)]
    factors = factors.union(new_factors)
    count = len(factors)
    if n not in factors:
        count += 1 # add one for the number itself if it was not prime
    return count

#Begining with 28, the 7th traingle number, it has six divisors.
n = 7
triangle = 28
divisors = 6
while (divisors < 500):
    n += 1
    triangle += n

    divisors = count_factors(triangle)

print(triangle)
