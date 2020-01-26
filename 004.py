def findLargestPal():
    """ Largest palindrome product

    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """

    largestPal = 0
    for x in reversed(range(100, 1000)):
        for y in reversed(range(100, 1000)):
            prod = x * y
            prod_str = str(prod)
            if (prod_str == prod_str[::-1]):
                if (prod > largestPal):
                    largestPal = prod
    return largestPal

print(findLargestPal())
