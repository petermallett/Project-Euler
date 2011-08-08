# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import time
start = time.clock()

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(a, b):
	return(int(a * b / gcd(a, b)))

num = 1
for x in range(2, 21):
	num = lcm(x, num)

print(num)

end = time.clock()
print(end-start)

