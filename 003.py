#find the largest prime factor of 600851475143
import math

number = 600851475143

def is_prime(n):
	if (n < 2):
		return False

	for x in range(2, int(math.sqrt(n))+1):
		if (n % x == 0):
			return False

	return True

def find_next_prime(n):
	x = n
	while(True):
		x += 1
		if (is_prime(x)):
			return x

half = int(number/2)

prime = 2
factors = []
answer = 0
while (answer == 0):
	if (number % prime == 0):
		factors.append(prime)
	prime = find_next_prime(prime)

	if (len(factors) == 4):
		print(factors)
		exit()