#What is the value of the first triangle number to have over five hundred divisors?

def count_divisors(n):
	count = 2
	for x in range(2, int(n/2)):
		if n % x == 0:
			count += 1
	return count

n = 7
triangle = 28
divisors = 5
while (divisors < 500):
	n += 1
	triangle += n

	divisors = count_divisors(triangle)

print(triangle)

