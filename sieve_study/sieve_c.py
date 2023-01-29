# sieve_c.py

from itertools import compress, count, cycle

def sieve_c():
	yield from (2, 3, 5)
	d = {}
	sel = (1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0)
	rem = (1, 7, 11, 13, 17, 19, 23, 29)
	for c in compress(count(7, 2), cycle(sel)):
		p = d.pop(c, None)
		if p is None:
			d[c * c] = c
			yield c
		else:
			x = c + 2 * p
			while x in d or x % 30 not in rem:
				x += 2 * p
			d[x] = p


pg = sieve_c()
for i in range(25):
	print(next(pg), end = ' ')
print()

for i in range(25):
	print(next(pg), end = ' ')
print()

