import unittest
from horror.src.skillcheck import *

class BasicTests(unittest.TestCase):
	"""test the functionality of the skillcheck class"""

	def testThrow(self):
		"""test throwing positive number of dices"""
		
		t = throw(4, -1)
		self.assertEqual(len(t), 3)
		for v in t:
			self.assertTrue(v > 0 and v < 7 and v%1 == 0)

	def testZeroThrow(self):
		"""test throwing zero dices"""

		t = throw(5, -5)
		self.assertEqual(t, [])

	def testMinusThrow(self):
		"""test throwing negative number of dices"""

		t = throw(2, -3)
		self.assertEqual(t, [])

	def testSuccess(self):
		"""test successful skill check"""

		t = [3, 5, 6]
		self.assertTrue(check(1, t))

	def testFailure(self):
		"""test failed skill check"""

		t = [2, 1, 3, 4]
		self.assertFalse(check(1, t))


def suite():
	suite = unittest.TestLoader().loadTestsFromTestCase(BasicTests)
	return suite


