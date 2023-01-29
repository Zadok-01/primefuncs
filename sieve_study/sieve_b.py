# sieve_b.py

from itertools import compress, count, cycle

def sieve_b():
	yield from (2, 3)
	d = {}
	sel = (1, 1, 0)
	rem = (1, 5)
	for c in compress(count(5, 2), cycle(sel)):
		p = d.pop(c, None)
		if p is None:
			d[c * c] = c
			yield c
		else:
			x = c + 2 * p
			while x in d or x % 6 not in rem:
				x += 2 * p
			d[x] = p


pg = sieve_b()
for i in range(25):
	print(next(pg), end = ' ')
print()

for i in range(25):
	print(next(pg), end = ' ')
print()

