from projecteuler import lcm

def smallestPositiveEvenlyDivisibleByAll(a, b):
    """ Smallest multiple

    2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?
    """

    start = a
    if start == 1:
        start = 2

    result = 1
    for x in range(start, b + 1):
        result = lcm(x, result)
    return result

print(smallestPositiveEvenlyDivisibleByAll(1, 20))
