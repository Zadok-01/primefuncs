# sieve_a.py

from itertools import count

def sieve_a():
	d = {}
	yield 2
	for c in count(3, 2):
		p = d.pop(c, None)
		if p is None:
			d[c * c] = c
			yield c
		else:
			#x = c + 2 * p
			x = c + 2 * p
			while x in d:
				x += 2 * p
			d[x] = p


pg = sieve_a()
for i in range(25):
	print(next(pg), end = ' ')
print()

for i in range(25):
	print(next(pg), end = ' ')
print()

