
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(a, b):
	return(int(a * b / gcd(a, b)))

