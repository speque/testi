# coding=utf8
import unittest
from horror.src.area import *
from horror.src.location import *

class BasicTests(unittest.TestCase):
	"""class for testing the functionality of the area class"""
	
	def testAddingAdjacentLocation(self):
		"""test adding an adjacent location for a street area"""
		s = area()
		l = location('Joukkila')
		s.addLocation(l)
		self.assertTrue(s.adjLocs.has_key(l.name))
		self.assertEqual(l, s.adjLocs[l.name])
	
	def testAddingAdjacentStreetArea(self):
		"""test adding an adjacent street area for a street area"""
		s = area()
		s2 = area()
		s.addArea(s2)
		self.assertTrue(s.adjAreas.has_key(s2.name))
		self.assertEqual(s2, s.adjAreas[s2.name])

	def testReachableAreas(self):
		"""test finding reachable street areas"""
		s1 = area('street1')
		s2 = area('street2')
		s3 = area('stret3')
		s4 = area('street4')

		s1.addArea(s2)
		s2.addArea(s1)
		s2.addArea(s3)
		s3.addArea(s2)
		s3.addArea(s4)
		s4.addArea(s3)

		r = s1.reachables(2)
		self.assertTrue(len(r) == 3)
		self.assertTrue(s2.name in r)
		self.assertTrue(s3.name in r)
		self.assertFalse(s4.name in r)

	def testReachableLocations(self):
		"""test finding reachable locations"""
		s1 = area('street1')
		s2 = area('street2')

		l1 = location('l1')
		l2 = location('l2')
		l3 = location('l3')

		s1.addLocation(l1)
		s1.addLocation(l2)
		s1.addArea(s2)
		s2.addLocation(l3)
		s2.addArea(s1)

		r = s1.reachables(1)
		self.assertEqual(len(r), 4)
		self.assertTrue(l1.name in r)
		self.assertTrue(l2.name in r)
		self.assertTrue(s2.name in r)
		self.assertFalse(l3.name in r)
	
	def testDistanceToSelf(self):
		"""test measuring the distance to area itself"""
		s = area('area')
		d = s.distanceTo('area')
		self.assertEqual(d, 0)

	def testDistanceToAdjacentLocation(self):
		"""test measuring the distance to an adjacent location"""
		s = area('area')
		l = location('location')
		s.addLocation(l)
		l.adjArea = s
		d = s.distanceTo('location')
		self.assertEqual(d, 1)
	
	def testDistanceToArea(self):
		"""test measuring the distance to an area"""
		s1 = area('street1')
		s2 = area('street2')
		s3 = area('stret3')
		s4 = area('street4')

		s1.addArea(s2)
		s2.addArea(s1)
		s2.addArea(s3)
		s3.addArea(s2)
		s3.addArea(s4)
		s4.addArea(s3)

		d = s1.distanceTo('street4')
		self.assertEqual(d, 3)

	def testDistanceToLocation(self):
		"""test measuring the distance to a location"""
		s1 = area('street1')
		s2 = area('street2')

		l1 = location('l1')
		l2 = location('l2')
		l3 = location('l3')

		s1.addLocation(l1)
		s1.addLocation(l2)
		s1.addArea(s2)
		s2.addLocation(l3)
		s2.addArea(s1)

		d = s1.distanceTo('l3')
		self.assertEqual(d, 2)

	def testDistanceToNowhere(self):
		"""test measuring the distance to a place that does not exist"""
		s = area('area')
		self.assertRaises(NoSuchDestinationFromAreaError, s.distanceTo, 'Nowhere')

def suite():
	suite = unittest.TestLoader().loadTestsFromTestCase(BasicTests)
	return suite

