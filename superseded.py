'All kinds of functions relating to factoring and the like.'

# Note: functions for primes and prime factors, elsewhere.


from functools import reduce
from operator import mul


# These are retained manily for historical interest.


def isfactor(f, n):
	'Returns True if f is a factor of n.'
	return not n % f



def _gcd(a, b):
	'Returns greatest common divisor (highest common factor) of a and b.'
	while b:
		a, b = b, a % b
	return abs(a)


def gcd(*a):
	'Returns greatest common divisor of arguments.'
	# available as math.gcd
	return reduce(_gcd, a)


def _lcm(a, b):
	'Returns lowest common multiple a and b.'
	return a * b // gcd(a, b)


def lcm(*a):
	'Returns lowest common multiple of arguments.'
	# available as math.lcm
	return reduce(_lcm, a)


def prod(iterable, start=1):
	'Returns the product of the elements of iterable.'
	# default inital value
	# available as math.prod
	return reduce(mul, iterable, start)


def factorial(n):
	'Returns factorial of n.'
	# available as math.factorial
	return prod(range(1, n+1))


def perm(n, r):
	'Returns the number of ways of choosing r items from a group of n items without repetition where order matters.'
	# available as math.perm
	return factorial(n) // factorial(n - r)


def comb(n, r):
	'Returns the number of ways of choosing r items from a group of n items without repetition and where order does not matter.'
	# available as math.comb
	return perm(n, r) // factorial(r)


def isqrt(n):
	'Returns the largest integer whose square does is not greater than n.'
	# n is a non-negative integer
	# available as math.isqrt
	if n == 0:
		return 0
	x, y = n, (n + 1) // 2
	while y < x:
		x, y = y, (y + n // y) // 2
	return x

