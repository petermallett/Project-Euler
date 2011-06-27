#Find the sum of all the primes below two million.
import math
import time
start = time.clock()

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
			
sum = 2
prime = 3
while(prime < 2000000):
	sum += prime
	prime = find_next_prime(prime)

print(sum)

end = time.clock()
print(end-start)
