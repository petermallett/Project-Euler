# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from projecteuler import lcm

num = 1
for x in range(2, 21):
	num = lcm(x, num)

print(num)

