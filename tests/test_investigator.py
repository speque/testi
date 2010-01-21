import unittest
from horror.src.investigator import *

class BasicTests(unittest.TestCase):
	"""class for testing the functionality of the investigator class"""	
	
	def testIncrementStaminaAtMax(self):
		"""test incrementing stamina by one when it is at maximum"""
		i = investigator()
		i.maxStamina = 7
		i.stamina = 7
		i.modifyStamina(1)
		self.assertEqual(i.stamina, 7)

	def testModifyingStamina(self):
		"""test decrementing stamina by two and then incrementing
		by one starting from maximum stamina"""
		i = investigator()
		i.maxStamina = 7
		i.stamina = 7
		i.modifyStamina(-2)
		i.modifyStamina(1)
		self.assertEqual(i.stamina, 6)

        def testIncrementSanityAtMax(self):
                """test incrementing sanity by two when it is at maximum"""
                i = investigator()
		i.maxSanity = 7
		i.sanity = 7
                i.modifySanity(2)
                self.assertEqual(i.sanity, 7)

        def testModifyingSanity(self):
                """test decrementing sanity by three and then incrementing
                by two starting from maximum sanity"""
                i = investigator()
		i.maxSanity = 7
		i.sanity = 7
                i.modifySanity(-3)
                i.modifySanity(2)
                self.assertEqual(i.sanity, 6)

	def testConsciousness(self):
		"""test conciousness"""
		i = investigator()
		i.stamina = 5
		self.assertTrue(i.isConscious())

	def testUnconsciousness(self):
		"""test unconsiciousness"""
		i = investigator()
		i.stamina = 0
		self.assertFalse(i.isConscious())

	def testSanity(self):
		"""test sanity"""
		i = investigator()
		i.sanity = 5
		self.assertTrue(i.isSane())

	def testInsanity(self):
		"""test insanity"""
		i = investigator()
		i.sanity = 0
		self.assertFalse(i.isSane())

	def testToString(self):
		"""test the string representation of an investigator"""
		i = investigator()
		i.name = 'Veijo Hietala'
		i.profession = 'Professor'
		i.maxStamina = 3
		i.stamina = 3
		i.maxSanity = 7
		i.sanity = 7
		i.focus = 2
		i.speedrow = (1, 2, 3, 4)
		i.speed = 2
		i.sneakRow = (4, 3, 2, 1)
		i.sneak = 3
		i.fightRow = (0, 1, 2, 3)
		i.fight = 1
		i.willRow = (5, 4, 3, 2)
		i.will = 4
		i.loreRow = (6, 5, 4, 3)
		i.lore = 5
		i.luckRow = (4, 3, 2, 1)
		i.luck = 3
		i.location = 'Turku'

		srep = i.toString()
		self.assertEqual(srep, \
		'Name: Veijo Hietala\nProfession: Professor\nStamina: 3\nSanity: 7' + \
		'\nFocus: 2\nLocation: Turku\n')


class SkillRelatedTests(unittest.TestCase):
	"""test functionality related to investigator skills"""

	def testIncrementSpeed(self):
		"""test incrementing speed skill from minimum four times"""
		i = investigator()
		i.speedRow = [0, 2, 4, 6]
		i.sneakRow = [7, 5, 3, 1]
		i.speed = 0
		i.sneak = 7
		i.focus = 3
		i.incrementSpeed()
		self.assertEqual(i.speed, 2)
		self.assertEqual(i.sneak, 5)
		self.assertEqual(i.focus, 2)
		i.incrementSpeed()
		self.assertEqual(i.speed, 4)
		self.assertEqual(i.sneak, 3)
		self.assertEqual(i.focus, 1)
		i.incrementSpeed()
		self.assertEqual(i.speed, 6)
		self.assertEqual(i.sneak, 1)
		self.assertEqual(i.focus, 0)
		i.incrementSpeed()
		self.assertEqual(i.speed, 6)
		self.assertEqual(i.sneak, 1)
		self.assertEqual(i.focus, 0)

	def testIncrementSneak(self):
		"""test incrementing speed skill from minimum four times"""
		i = investigator()
		i.speedRow = [0, 2, 4, 6]
		i.sneakRow = [7, 5, 3, 1]
		i.speed = 6
		i.sneak = 1
		i.focus = 3
		i.incrementSneak()
		self.assertEqual(i.speed, 4)
		self.assertEqual(i.sneak, 3)
		self.assertEqual(i.focus, 2)
		i.incrementSneak()
		self.assertEqual(i.speed, 2)
		self.assertEqual(i.sneak, 5)
		self.assertEqual(i.focus, 1)
		i.incrementSneak()
		self.assertEqual(i.speed, 0)
		self.assertEqual(i.sneak, 7)
		self.assertEqual(i.focus, 0)
		i.incrementSneak()
		self.assertEqual(i.speed, 0)
		self.assertEqual(i.sneak, 7)
		self.assertEqual(i.focus, 0)

	def testIncrementFight(self):
		"""test incrementing fight skill from minimum four times"""
		i = investigator()
		i.fightRow = [0, 2, 4, 6]
		i.willRow = [7, 5, 3, 1]
		i.fight = 0
		i.will = 7
		i.focus = 3
		i.incrementFight()
		self.assertEqual(i.fight, 2)
		self.assertEqual(i.will, 5)
		self.assertEqual(i.focus, 2)
		i.incrementFight()
		self.assertEqual(i.fight, 4)
		self.assertEqual(i.will, 3)
		self.assertEqual(i.focus, 1)
		i.incrementFight()
		self.assertEqual(i.fight, 6)
		self.assertEqual(i.will, 1)
		self.assertEqual(i.focus, 0)
		i.incrementFight()
		self.assertEqual(i.fight, 6)
		self.assertEqual(i.will, 1)
		self.assertEqual(i.focus, 0)

	def testIncrementWill(self):
		"""test incrementing will skill from minimum four times"""
		i = investigator()
		i.fightRow = [0, 2, 4, 6]
		i.willRow = [7, 5, 3, 1]
		i.fight = 6
		i.will = 1
		i.focus = 3
		i.incrementWill()
		self.assertEqual(i.fight, 4)
		self.assertEqual(i.will, 3)
		self.assertEqual(i.focus, 2)
		i.incrementWill()
		self.assertEqual(i.fight, 2)
		self.assertEqual(i.will, 5)
		self.assertEqual(i.focus, 1)
		i.incrementWill()
		self.assertEqual(i.fight, 0)
		self.assertEqual(i.will, 7)
		self.assertEqual(i.focus, 0)
		i.incrementWill()
		self.assertEqual(i.fight, 0)
		self.assertEqual(i.will, 7)
		self.assertEqual(i.focus, 0)

	def testIncrementLore(self):
		"""test incrementing lore skill from minimum four times"""
		i = investigator()
		i.loreRow = [0, 2, 4, 6]
		i.luckRow = [7, 5, 3, 1]
		i.lore = 0
		i.luck = 7
		i.focus = 3
		i.incrementLore()
		self.assertEqual(i.lore, 2)
		self.assertEqual(i.luck, 5)
		self.assertEqual(i.focus, 2)
		i.incrementLore()
		self.assertEqual(i.lore, 4)
		self.assertEqual(i.luck, 3)
		self.assertEqual(i.focus, 1)
		i.incrementLore()
		self.assertEqual(i.lore, 6)
		self.assertEqual(i.luck, 1)
		self.assertEqual(i.focus, 0)
		i.incrementLore()
		self.assertEqual(i.lore, 6)
		self.assertEqual(i.luck, 1)
		self.assertEqual(i.focus, 0)

	def testIncrementLuck(self):
		"""test incrementing luck skill from minimum four times"""
		i = investigator()
		i.loreRow = [0, 2, 4, 6]
		i.luckRow = [7, 5, 3, 1]
		i.lore = 6
		i.luck = 1
		i.focus = 3
		i.incrementLuck()
		self.assertEqual(i.lore, 4)
		self.assertEqual(i.luck, 3)
		self.assertEqual(i.focus, 2)
		i.incrementLuck()
		self.assertEqual(i.lore, 2)
		self.assertEqual(i.luck, 5)
		self.assertEqual(i.focus, 1)
		i.incrementLuck()
		self.assertEqual(i.lore, 0)
		self.assertEqual(i.luck, 7)
		self.assertEqual(i.focus, 0)
		i.incrementLuck()
		self.assertEqual(i.lore, 0)
		self.assertEqual(i.luck, 7)
		self.assertEqual(i.focus, 0)

def suite():
	suite = unittest.TestLoader().loadTestsFromTestCase(BasicTests)
	suite.addTests(unittest.TestLoader().loadTestsFromTestCase(SkillRelatedTests))
	return suite
	
