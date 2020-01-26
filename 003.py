from projecteuler import find_prime_factors

def getLargestPrimeFactor(n):
    """ Largest prime factor

    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """

    pf = find_prime_factors(number)
    return pf[-1]

number = 600851475143
print(getLargestPrimeFactor(number))
