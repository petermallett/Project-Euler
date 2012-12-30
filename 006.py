# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

sum, sum_of_squares = 0, 0

for x in range(1, 101):
    sum += x
    sum_of_squares += x * x

square_of_sum = sum * sum

print(square_of_sum - sum_of_squares)
