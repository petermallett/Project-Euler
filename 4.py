#Find the largest palindrome made from the product of two 3-digit numbers.

pal = 0
for x in reversed(range(100, 1000)):
	for y in reversed(range(100, 1000)):
		prod = x * y
		prod_str = str(prod)
		if (prod_str == prod_str[::-1]):
			if (prod > pal):
				pal = prod
print (pal)