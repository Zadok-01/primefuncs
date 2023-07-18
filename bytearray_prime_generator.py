from math import isqrt
from itertools import compress

def primes_w2(n):
	'Primes to n inclusive'
	# primes(19) --> 2 3 5 7 11 13 17 19
	n += 1
	sieve = bytearray((0, 1)) * (n // 2)
	sieve[:3] = 0, 0, 0
	for p in compress(range(isqrt(n) + 1), sieve):
		sieve[p*p : n : p+p] = bytes(len(range(p*p, n, p+p)))
	sieve[2] = 1
	return (i for i, x in enumerate(sieve) if x) if n > 2 else iter([])


def primes_w6(n):
	'Primes to n inclusive'
	# primes(19) --> 2 3 5 7 11 13 17 19
	if n < 2:
		return iter([])
	sieve = bytearray((0, 1, 0, 0, 0, 1)) * (n // 6 + 1)
	sieve[1] = 0
	for p in compress(range(isqrt(n) + 1), sieve):
		sieve[p*p : n+1 : p+p] = bytes(len(range(p*p, n+1, p+p)))
	sieve[2:4] = 1, 1
	while len(sieve) > n + 1:
		sieve.pop()
	return (i for i, x in enumerate(sieve) if x)


def primes_w30(n):
	'Primes to n inclusive'
	# primes(19) --> 2 3 5 7 11 13 17 19
	if n < 2:
		return iter([])
	sieve = bytearray((0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1)) * (n // 30 + 1)
	sieve[1] = 0
	for p in compress(range(isqrt(n) + 1), sieve):
		sieve[p*p : n+1 : p+p] = bytes(len(range(p*p, n+1, p+p)))
	sieve[2:6] = 1,1,0,1
	while len(sieve) > n + 1:
		sieve.pop()
	return (i for i, x in enumerate(sieve) if x)


primes = primes_w6


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


'''
for a in range(106):
	p = [*primes(a)]
	print(a, p, len(p))

print('------')
'''

print(*primes(19))
print(*factor(45))

