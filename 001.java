//find the sum of numbers less than 1000 which are divisible by 3 or 5

class Problem001 {
	public static void main(String[] args) {
		int sum = 0;
		for (int x = 1; x < 1000; x++)
		{
			if (x % 3 == 0 || x % 5 == 0)
			{
				sum += x;
			}
		}
		System.out.println(sum);
	}
}

