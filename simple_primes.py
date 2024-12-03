'Simple prime functions'


from itertools import cycle, compress, count, islice, takewhile


__all__ = 	(
			'primes', 
			'primes_quant', 
			'primes_max', 
			'isprime', 
			)


def primes():
	'Generates infinite sequence of primes'
	# Note: p_gen is an infinite generator
	yield from (2, 3, 5)
	d = {}
	sel = 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0
	rem = 1, 7, 11, 13, 17, 19, 23, 29
	for c in compress(count(7, 2), cycle(sel)):
		p = d.pop(c, None)
		if p:
			x = c + 2 * p
			while x in d or x % 30 not in rem:
				x += 2 * p
			d[x] = p
		else:
			d[c * c] = c
			yield c


def primes_quant(k):
	'Generates first k primes'
	return islice(primes(), k)


def primes_max(max):
	'Generates primes below max'
	pred = lambda x: x < max
	yield from takewhile(pred, primes())


def isprime(x):
	'Returns True if x is prime'
	return x in primes_max(x + 1)


if __name__ == '__main__':
	# Tests functions above
	print([*primes_max(20)])    # [2, 3, 5, 7, 11, 13, 17, 19]
	print([*primes_quant(10)])  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
	print(isprime(12))          # False
	print(isprime(13))          # True

