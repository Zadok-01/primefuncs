'Unit tests for primefuncs4'


from unittest import TextTestRunner, TestSuite, TestCase
from primefuncs4 import *


class Test_Simple(TestCase):
	
	def test_primes(self):
		max = 20
		result = primes(max)
		self.assertEqual(result, [2, 3, 5, 7, 11, 13, 17, 19])
	
	
	def test_primesq(self):
		quant = 6
		result = primesq(quant)
		self.assertEqual(result, [2, 3, 5, 7, 11, 13])
	
	
	def test_isprime(self):
		n = 13
		result = is_prime(n)
		self.assertEqual(result, True)
		n = 14
		result = is_prime(n)
		self.assertEqual(result, False)
	
	
	def test_pfacts(self):
		n = 24
		result = pfacts(n)
		self.assertEqual(result, [2, 2, 2, 3])
	
	
	def test_pfacts2(self):
		n = 24
		result = pfacts(n)
		self.assertEqual(result, [2, 2, 2, 3])
	
	
	def test_facts(self):
		n = 24
		result = facts(n)
		self.assertEqual(result, [1, 2, 3, 4, 6, 8, 12, 24])
	
	
	def test_facts2(self):
		n = 24
		result = facts2(n)
		self.assertEqual(result, [1, 2, 3, 4, 6, 8, 12, 24])


class Test_Prime(TestCase):
	
	def test_primequant(self):
		k = 8
		result = [*primequant(k)]
		self.assertEqual(result, [2, 3, 5, 7, 11, 13, 17, 19])
	
	
	def test_prime(self):
		n = 5
		result = prime(n)
		self.assertEqual(result, 11)
		n = 9
		result = prime(n)
		self.assertEqual(result, 23)
	
	
	def test_primorial(self):
		n = 5
		result = primorial(n)
		self.assertEqual(result, 2310)
	
	
	def test_primerange(self):
		a = 6
		b = 18
		result = [*primerange(a, b)]
		self.assertEqual(result, [7, 11, 13, 17])
	
	
	def test_prime_count(self):
		x = 13
		result = prime_count(x)
		self.assertEqual(result, 5)
	
	
	def test_prevprime(self):
		n = 11
		result = prevprime(n)
		self.assertEqual(result, 7)
		n = 12
		result = prevprime(n)
		self.assertEqual(result, 11)
	
	
	def test_nextprime(self):
		n = 10
		result = nextprime(n)
		self.assertEqual(result, 11)
		n = 11
		result = nextprime(n)
		self.assertEqual(result, 13)
	
	
	def test_iscoprime(self):
		a = 12
		b = 4
		result = iscoprime(a, b)
		self.assertEqual(result, False)
		b = 5
		result = iscoprime(a, b)
		self.assertEqual(result, True)
	
	
	def test_totient(self):
		n = 12
		result = totient(n)
		self.assertEqual(result, 4)
		n = 13
		result = totient(n)
		self.assertEqual(result, 12)


class Test_Factors(TestCase):
	
	def test_pfactors(self):
		n = 24
		result = [*pfactors(n)]
		self.assertEqual(result, [2, 2, 2, 3])
	
	
	def test_pfactors_mult(self):
		n = 24
		result = pfactors_mult(n)
		self.assertEqual(result, [(2, 3), (3, 1)])
	
	
	def test_factors(self):
		n = 24
		result = facts2(n)
		self.assertEqual(result, [1, 2, 3, 4, 6, 8, 12, 24])


class Test_Misc(TestCase):
	
	def test_prevodd(self):
		n = 7
		result = prevodd(n)
		self.assertEqual(result, 5)
		n = 6
		result = prevodd(n)
		self.assertEqual(result, 5)
	
	
	def test_nextodd(self):
		n = 7
		result = nextodd(n)
		self.assertEqual(result, 9)
		n = 8
		result = nextodd(n)
		self.assertEqual(result, 9)
	
	
	def test_preveven(self):
		n = 7
		result = preveven(n)
		self.assertEqual(result, 6)
		n = 6
		result = preveven(n)
		self.assertEqual(result, 4)
	
	
	def test_nexteven(self):
		n = 7
		result = nexteven(n)
		self.assertEqual(result, 8)
		n = 8
		result = nexteven(n)
		self.assertEqual(result, 10)
	
	
	def test_issquare(self):
		n = 7
		result = issquare(n)
		self.assertEqual(result, False)
		n = 9
		result = issquare(n)
		self.assertEqual(result, True)
	
	
	def test_isqrt_u(self):
		n = 7
		result = isqrt_u(n)
		self.assertEqual(result, 3)
		n = 9
		result = isqrt_u(n)
		self.assertEqual(result, 3)
	
	
	def test_isqrt_lt(self):
		n = 7
		result = isqrt_lt(n)
		self.assertEqual(result, 2)
		n = 9
		result = isqrt_lt(n)
		self.assertEqual(result, 2)
	
	
	def test_isqrt_gt(self):
		n = 7
		result = isqrt_gt(n)
		self.assertEqual(result, 3)
		n = 9
		result = isqrt_gt(n)
		self.assertEqual(result, 4)
	
	
	def test_powerset(self):
		a = ['A', 'B', 'C']
		n = 24
		result = [*powerset(a)]
		self.assertEqual(result, [(), ('A',), ('B',), ('C',), ('A', 'B'), ('A', 'C'), ('B', 'C'), ('A', 'B', 'C')])
	
	
	def test_ilog(self):
		x = 100
		b = 10
		result = ilog(x, b)
		self.assertEqual(result, 2)
		x = 1000
		result = ilog(x, b)
		self.assertEqual(result, 3)
	
	
	def test_imod(self):
		a = 5
		n = 7
		result = imod(a, n)
		self.assertEqual(result, 3)


def suite_simple():
	suite = TestSuite()
	suite.addTest(Test_Simple('test_primes'))
	suite.addTest(Test_Simple('test_primesq'))
	suite.addTest(Test_Simple('test_isprime'))
	suite.addTest(Test_Simple('test_pfacts'))
	suite.addTest(Test_Simple('test_pfacts2'))
	suite.addTest(Test_Simple('test_facts'))
	suite.addTest(Test_Simple('test_facts2'))
	return suite


def suite_prime():
	suite = TestSuite()
	suite.addTest(Test_Prime('test_primequant'))
	suite.addTest(Test_Prime('test_prime'))
	suite.addTest(Test_Prime('test_primorial'))
	suite.addTest(Test_Prime('test_primerange'))
	suite.addTest(Test_Prime('test_prime_count'))
	suite.addTest(Test_Prime('test_prevprime'))
	suite.addTest(Test_Prime('test_nextprime'))
	suite.addTest(Test_Prime('test_iscoprime'))
	suite.addTest(Test_Prime('test_totient'))
	return suite


def suite_factors():
	suite = TestSuite()
	suite.addTest(Test_Factors('test_pfactors'))
	suite.addTest(Test_Factors('test_pfactors_mult'))
	suite.addTest(Test_Factors('test_factors'))
	return suite


def suite_misc():
	suite = TestSuite()
	suite.addTest(Test_Misc('test_prevodd'))
	suite.addTest(Test_Misc('test_nextodd'))
	suite.addTest(Test_Misc('test_preveven'))
	suite.addTest(Test_Misc('test_nexteven'))
	suite.addTest(Test_Misc('test_issquare'))
	suite.addTest(Test_Misc('test_isqrt_u'))
	suite.addTest(Test_Misc('test_isqrt_lt'))
	suite.addTest(Test_Misc('test_isqrt_gt'))
	suite.addTest(Test_Misc('test_powerset'))
	suite.addTest(Test_Misc('test_ilog'))
	suite.addTest(Test_Misc('test_imod'))
	return suite


if __name__ == '__main__':
	runner = TextTestRunner(verbosity=2)
	runner.run(suite_simple())
	runner.run(suite_prime())
	runner.run(suite_factors())
	runner.run(suite_misc())

