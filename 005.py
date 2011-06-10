# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import time
start = time.clock()

def test_divisors(n):
	#dont test 1, 2, 5, 10 or 20
	list = [3,4,6,7,8,9,11,12,13,14,15,16,17,18,19]
	for x in list:
		if (n % x != 0):
			return False

	return True

a = 20
while(not test_divisors(a)):
	a += 20

print(a)

end = time.clock()
print(end-start)
