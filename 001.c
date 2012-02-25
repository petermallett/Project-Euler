//find the sum of numbers less than 1000 which are divisible by 3 or 5
#include <stdio.h>

int main(char argc, char* argv[])
{
	int sum = 0, x = 1;
	for (x = 1; x < 1000; x++)
	{
		if (x % 3 == 0 || x % 5 == 0)
		{
			sum += x;
		}
	}
	printf("%d", sum);
	return 0;
}

