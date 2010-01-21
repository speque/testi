import unittest
from horror.src.location import *
from horror.src.area import *

class BasicTests(unittest.TestCase):
	"""class for testing the functionality of the location class"""
	
	def testReachableArea(self):
		"""test finding the area reachable from a location"""
		l = location('location')
		s = area('street')
		l.adjArea = s
		s.addLocation(l)
		
		r = l.reachables(1)
		self.assertTrue(s.name in r)
		self.assertTrue(l.name in r)
		self.assertEqual(len(r), 2)

	def testDistanceToSelf(self):
		"""test measuring distance to location itself"""
		l = location('location')
		d = l.distanceTo('location')
		self.assertEqual(d, 0)
	
	def testDistanceToadjacentArea(self):
		"""test measuring the distance to adjacent area"""
		l = location('location')
		s = area('area')
		l.adjArea = s
		s.addLocation(l)
		d = l.distanceTo('area')
		self.assertEqual(1, d)

	def testDistanceToNowhere(self):
		"""test measuring distance to a place that does not exist"""
		l = location('location')
		self.assertRaises(NoSuchDestinationFromLocationError, l.distanceTo, 'Nowhere')

def suite():
	suite = unittest.TestLoader().loadTestsFromTestCase(BasicTests)
	return suite
