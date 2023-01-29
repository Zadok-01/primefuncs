'Testing of the isprime function in primefuncs4'


####  WARNING  ####
#
# This program is to verify the isprime function against a naive function.
# A large number of tests are performed and this could take some 
# considerable time.  This is especially so for the second part where very 
# large values are used.  The naive function will slow down the process, 
# but it needed to provide proper validation.


from primefuncs4 import pfacts2, isprime
from random import randint


def isprime_naive(n):
	# Simple test onbly suitable for small values of n
	# This checks that n has no prime factors other than itself
	return [*pfacts2(n)] == [n]


# Run tests
# Blocks of consecutive numbers
for e in range(7):  ###### 7
	size, naive_count, discovered = 10 ** e, 0, 0
	for n in range(size):
		if isprime_naive(n):
			naive_count += 1
		if isprime(n):
			discovered += 1
	msg = 'Primes below {:,}: \t\tActual: {:,} \t\t Found: {:,}'
	print(msg.format(size, naive_count, discovered))
print()


# Random selection of higher values to test
size, naive_count, discovered = int(5e5), 0, 0
min, max = map(int, (1e6, 1e10))
for _ in range(size):
	n = randint(min, max)
	if isprime_naive(n):
		naive_count += 1
	if isprime(n):
		discovered += 1
msg = 'In a selection of {:,} numbers between {:,} and {:,}'
print(msg.format(size, min, max))
msg = 'there were {:,} primes and {:,} were found'
print(msg.format(naive_count, discovered))

