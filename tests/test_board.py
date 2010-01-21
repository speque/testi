import unittest
from horror.src.board import *
from horror.src.location import *
from horror.src.area import *

class BasicTests(unittest.TestCase):
	"""class for testing the functionality of the board class"""

	def testAddingLocation(self):
		"""test adding a location on a board"""
		b = board()
		l = location()
		l.name = 'Location'
		b.addLocation(l)
		self.assertTrue(l.name in b.locs)
		self.assertEqual(l, b.locs[l.name])

	def testAddingStreet(self):
		"""test adding a street location on a board"""
		b = board()
		s = area()
		s.name = 'Street'
		b.addStreet(s)
		self.assertTrue(s.name in b.streets)
		self.assertEqual(s, b.streets[s.name])

def suite():
	suite = unittest.TestLoader().loadTestsFromTestCase(BasicTests)
	return suite
