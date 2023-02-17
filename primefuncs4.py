'Collection of functions dealing with primes, factors and related topics.'


__library__ = 'primefuncs'
__version__ = '4.00'


_all_simple = ('primes', 'primesq', 'is_prime', 'pfacts', 'pfacts2', 
			'facts', 'facts2')

_all_prime = ('p_gen', 'primequant', 'prime', 'primorial', 'primerange', 
			'prime_count', 'isprime', 'prevprime', 'nextprime', 'randprime', 
			'iscoprime', 'totient')

_all_factors = ('pfactors', 'pfactors_mult', 'factors')

_all_misc = ('prevodd', 'nextodd','preveven', 'nexteven', 'issquare', 
			'isqrt_u', 'isqrt_lt', 'isqrt_gt', 'powerset', 'ilog', 'imod')

__all__ = _all_simple + _all_prime + _all_factors + _all_misc


from itertools import chain, combinations, count, cycle, dropwhile, \
					islice,takewhile
from math import gcd, isqrt, prod
from random import randrange


####  Simple  ####

# These function are intended for use with small arguments or on only 
# a few occasions.  Otherwise, it may be worth considering the functions 
# in later sections.


def primes(max):
	'Return list of primes up to a mximum value, inclusive.'
	if max < 2:
		return []
	primes = [2]
	for candidate in range(3, max + 1, 2):
		isprime = True
		for divisor in primes:
			if divisor ** 2 > candidate:
				break
			if not candidate % divisor:
				isprime = False
				break
		if isprime:
			primes.append(candidate)
	return primes


def primesq(quant):
	'Return list of primes up to a mximum value, inclusive.'
	if quant < 1:
		return []
	primes = [2]
	if quant < 2:
		return primes
	for candidate in count(3, 2):
		if len(primes) == quant:
			break
		flag = True
		for divisor in primes:
			if divisor ** 2 > candidate:
				break
			if not candidate % divisor:
				flag = False
				break
		if flag == True:
			primes.append(candidate)
	return primes


def is_prime(n):
	'Determine whether a number is prime.'
	if n < 4:
		return n > 1
	if not n % 2 or not n % 3:
		return False
	for i in range(5, int(n ** 0.5) + 1, 6):
		if not n % i or not n % (i + 2):
			return False
	return True


def pfacts(n):
	'Returns list of all (repeated) prime factors of n.'
	d = 2
	pf = []
	while d * d <= n:
		if n % d:
			d += 1
		else:
			n //= d
			pf.append(d)
	if n > 1:
		pf.append(n)
	return pf


def pfacts2(n):
	'Generator yielding an iterable of all (repeated) the prime factors of n.'
	d = 2
	increments = chain((1, 2, 2), cycle((4, 2, 4, 2, 4, 6, 2, 6)))
	for incr in increments:
		if d * d > n:
			break
		while not n % d:
			yield d
			n //= d
		d += incr
	if n > 1:
		yield n


def facts(n):
	'Find all the factors of n.'
	return [d for d in range(1, n+1) if not n % d]


def facts2(n):
	'Find all the factors of n.'
	step = 2 if n & 1 else 1  # all factors of odd n are also odd
	f = sum(([d, n // d] for d in range(1, isqrt_gt(n), step) if not n % d), [])
	if issquare(n):
		f.pop()
	return sorted(f)


####  Prime Number Functions  ####


def p_gen():
	'Generator yielding an infinite sequence of primes.'
	# Note: p_gen is an infinite generator.
	yield from (2, 3, 5)
	d = {}
	steps = cycle((4, 2, 4, 2, 4, 6, 2, 6))
	rems = {1, 7, 11, 13, 17, 19, 23, 29}
	c = 7
	for step in steps:
		p = d.pop(c, None)
		if p is None:
			d[c * c] = c
			yield c
		else:
			x = c + 2 * p
			while x in d or x % 30 not in rems:
				x += 2 * p
			d[x] = p
		c += step


def primequant(k):
	'Generates a given quantity of primes.'
	return islice(p_gen(), k)


def prime(n):
	'Return the nth prime (prime(1) == 2).'
	return next(islice(p_gen(), n - 1, n))


def primorial(n):
	'Return product of first n primes.'
	n = int(n)
	if n < 0:
		raise ValueError('Argument of primorial cannot be negative')
	if n == 0:
		return 1
	return prod(primequant(n))


def primerange(a, b=None):
	'Generate all prime numbers in the range [2, a) or [a, b).'
	if b is None:
		a, b = 2, a
	if a >= b:
		return []
	a, b = map(int, (a, b))
	lo = lambda x: x < a
	hi = lambda x: x < b
	return dropwhile(lo, takewhile(hi, p_gen()))


def prime_count(x):
	'Return number of primes < x'
	return len(list(primerange(x)))


def isprime(n):
	'Determine whether a number is prime.'
	# Check argument is integer
	if type(n) != int:
		raise TypeError('isprime argument not an integer')
	
	# Deal with small n by divisor checks
	if n < 2:
		return False
	a = (2, 3, 5)
	if n in a:
		return True
	if any(not n % d for d in a):
		return False
	if n < 49:
		return True  # 49 == 7 ** 2
	a = (1, 5)
	if n % 6 not in a:
		return False
	a = (7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
	if n in a:
		return True
	if any(not n % d for d in a):
		return False
	if n < 2809:
		return True  # 2809 == 53 ** 2
	a = (1, 7, 11, 13, 17, 19, 23, 29)
	if n % 30 not in a:
		return False
	a = (53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
	if n in a:
		return True
	if any(not n % d for d in a):
		return False
	if n < 10201:
		return True  # 10201 == 101 ** 2
	
	# Simple use of Fermat test
	pseudo_primes = (31621, 42799, 49141, 49981, 60701, 83333, 88357, 90751)
	# These are pseudoprimes whose prime divisors are all greater than 100
	if n <= 101101:
		return pow(2, n, n) == 2 and n not in pseudo_primes
	
	# Miller-Rabin test for larger n
	s, d = 0, n - 1
	while not d % 2:
		s, d = s + 1, d >> 1
	t = (2_047, 1_373_653, 25_326_001, 3_215_031_751, 2_152_302_898_747, 
			3_474_749_660_383, 341_550_071_728_321, 341_550_071_728_321, 
			3_825_123_056_546_413_051, 3_825_123_056_546_413_051, 
			3_825_123_056_546_413_051, 318_665_857_834_031_151_167_461, 
			3_317_044_064_679_887_385_961_981)
	for k, t in enumerate(t):
		if t > n:
			return not any(_iscomposite(n, s, d, a) for a in primequant(k + 1))
	return not any(_iscomposite(n, s, d, a) for a in primequant(20))
	# The constant governs the size of n before inaccuracy appears
	
	'''
	If Miller-Rabin (or similar) is not used then some form of backstop 
	is required.  In this case a number of Fermat tests are performed with 
	randomly selected bases.
	'''
	# Fermat test used probabilistically
	return not any(pow(r := randint(2, n - 1), n, n) != r for _ in range(8))
	# Increasing the constant in range improves accuracy
	'''
	Equivalent statement if assignment cannot be made using the 
	walrus (:=) operator.
	return not any(pow(randint(2, n - 2), n - 1, n) != 1 for _ in range(8))
	'''


def _iscomposite(n, s, d, a):
	# Helper function for Miller-Rabin test
	if pow(a, d, n) == 1:
		return False
	for i in range(s):
		if pow(a, 2 ** i * d, n) == n - 1:
			return False
	return True  # n is definitely composite


def prevprime(n):
	'Return the largest prime smaller than n.'
	# If there is no previous prime, the return value is None
	if n < 3:
		return None
	if 2 < n < 6:
		return (2, 3, 3)[n - 3]
	n = prevodd(n)
	r = n % 6
	if r == 5:
		if isprime(n):
			return n
		n -= 4
	if r == 3:
		n -= 2
	for m in range(n, 6, -6):
		for d in (0, 2):
			if isprime(p := m - d): return p


def nextprime(n):
	'Returns the smallest prime greater than n.'
	if n < 2:
		return 2
	for p in (3, 5):
		if n < p:
			return p
	n = nextodd(n)
	r = n % 6
	if r == 1:
		if isprime(n):
			return n
		n += 4
	if r == 3: n += 2
	for m in count(n, 6):
		for d in (0, 2):
			if isprime(p := m + d): return p


def randprime(a, b):
	'Find a random prime in the range [a, b], inclusive.'
	# If there is no prime in the range, the return value is None
	r = randrange(a, b)
	if isprime(r):
		return r
	r = nextprime(r)
	if r <= b:
		return r
	r = prevprime(r)
	if r >= a:
		return r
	return None


def iscoprime(a, b):
	'Determine whether a is coprime to b.'
	return gcd(a, b) == 1


def totient(n):
	"Return Euler's Totient of n."
	# Euler's Totient is the count of integers coprime with n in the range [1, n]
	return sum(iscoprime(n, i) for i in range(n))


####  Factors  ####


def pfactors(n):
	'Generator yielding an iterable of all (repeated) the prime factors of n.'
	p = iter(p_gen())
	while (d := next(p)) ** 2 <= n:
		while not n % d:
			yield d
			n //= d
	if n > 1:
		yield n


def pfactors_mult(n):
	'Returns list of tuples giving prime factors with multiplicities'
	pf = list(pfactors(n))
	return sorted((f, pf.count(f)) for f in set(pf))


def factors(n):
	'Returns all the factors of n.'
	return sorted(set(prod(group) for group in powerset(pfactors(n))))


####  Miscellaneous Functions  ####


def prevodd(n):
	'Return next smaller odd number.'
	# Same as return n - 2 if n % 2 else n - 1
	return n - 2 | 1


def nextodd(n):
	'Return next higher odd number.'
	# Same as return n + 2 if n % 2 else n + 1
	return n + 1 | 1


def preveven(n):
	'Return next smaller even number.'
	# Same as return n - 1 if n % 2 else n - 2
	return (n - 3 | 1) + 1


def nexteven(n):
	'Return next higher even number'
	# Same as return n + 1 if n % 2 else n + 2
	return (n | 1) + 1


def issquare(n):
	'Determine whether a number is a perfect square.'
	return isqrt(n) ** 2 == n


def isqrt_u(n):
	'Return integer whose square is greater than or equal to n.'
	return 1 + isqrt(n - 1)
	'''Note:  The counterpart that returns the interger whose square is 
		less than or equal to n is simply isqrt from the standard math 
		module.'''


def isqrt_lt(n):
	'Return integer whose square is strictly less than n.'
	return isqrt(n - 1)


def isqrt_gt(n):
	'Return integer whose square is strictly greater than n.'
	return 1 + isqrt(n)


def powerset(iterable):
	'powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)'
	s = tuple(iterable)
	return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
	
	# Can use the version below if iterable is of known length, i.e. if it 
	# is a list.  This won't work if it is the output of a generator 
	# because all the results need to be collected first in order to find 
	# the "length" of the sequence.  In that case use the version above.
	'''
	for r in range(len(iterable)+1):
		yield from combinations(iterable, r)
	'''


def ilog(x, b):
	'Returns the greatest integer p such that b ** p <= x.'
	p = 0
	while x >= b:
		x /= b
		p += 1
	return p


def imod(a, n):
	'Returns the modular multiplicative inverse of a modulo n.'
	# i.e. finds the value x such that (a * x) % n == 1
	# Note: a and n must be coprime, i.e gcd(a, n) == 1
	c = 1
	while c % a > 0:
		c += n
	return c // a

