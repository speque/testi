class board:
	"""class modeling a board for the game"""

	def __init__(self):
		self.locs = {}
		self.streets = {}

	def addLocation(self, l):
		"""add a location on the board"""
		self.locs[l.name] = l

	def addStreet(self, s):
		"""add a street area on the board"""
		self.streets[s.name] = s

