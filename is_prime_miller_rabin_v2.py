# Alternate Miller Rabin Test

import random

def is_prime(n, k=5):
	"""
	Miller-Rabin primality test.

	Args:
		n (int): number to test for primality.
		k (int): number of iterations to run the test.

	Returns:
		True if n is probably prime, False otherwise.
	"""
	if n == 2 or n == 3:
		return True
	if n <= 1 or n % 2 == 0:
		return False

	# Write n-1 as 2^r*d
	r, d = 0, n - 1
	while d % 2 == 0:
		r += 1
		d //= 2

	# Run the test k times
	for _ in range(k):
		a = random.randint(2, n - 2)
		x = pow(a, d, n)
		if x == 1 or x == n - 1:
			continue
		for _ in range(r - 1):
			x = pow(x, 2, n)
			if x == n - 1:
				break
		else:
			return False
	return True
