from math import isqrt
from itertools import compress


def primes(n):
	'Primes to n inclusive'
	# primes(19) --> 2 3 5 7 11 13 17 19
	if n < 2:
		return iter([])
	data = bytearray((0, 1, 0, 0, 0, 1)) * (n // 6 + 1)
	data[1] = 0
	limit = isqrt(n) + 1
	for p in compress(range(limit), data):
		data[p*p : n+1 : p+p] = bytes(len(range(p*p, n+1, p+p)))
	data[2:4] = 1, 1
	while len(data) > n + 1:
		data.pop()
	return (i for i, x in enumerate(data) if x)


def factor(n):
	'Prime factors of n'
	# factor(45) --> 3 3 5
	for prime in primes(isqrt(n)):
		while True:
			quotient, remainder = divmod(n, prime)
			if remainder:
				break
			yield prime
			n = quotient
			if n == 1:
				return
	if n > 1:
		yield n


print(*primes(19))
print(*factor(45))

