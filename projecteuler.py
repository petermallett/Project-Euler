def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(a, b):
    return(int(a * b / gcd(a, b)))

def sieve(n):
    """ Calculates primes up to n and returns them in a list. """
    s = list(range(3, n + 1, 2))
    primes = [2]
    number_limit = n + 1
    index_limit = s.index(s[-1])
    i = 0
    while True:
        while not s[i]:
            i += 1
        primes.append(s[i])
        m = s[i]
        if m**2 > number_limit:
            s[i] = 0
            primes += [prime for prime in s if prime != 0]
            break
        ind = int((m * (m - 1) / 2) + i)
        while (ind <= index_limit):
            s[ind] = 0
            ind += m
        s[i] = 0
    return primes

def find_prime_factors(n):
    factors = []

    while n != 1:
        d = 2

        while n % d != 0:
            d += 1

        factors.append(d)
        n /= d

    return factors
