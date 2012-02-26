#find the sum of even fibonacci sequence members less than 4 million
a, b = 1, 1
sum = 0
while (a < 4000000):
	if (a % 2 == 0):
		sum += a

	temp = a
	a = a + b
	b = temp

print(sum)

