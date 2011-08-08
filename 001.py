#find the sum of numbers less than 1000 which are divisible by 3 or 5
sum = 0
for x in range(1, 1000):
	if (x % 3 == 0 or x % 5 == 0):
		sum += x
print(sum)

