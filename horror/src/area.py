class AreaError(Exception): pass
class NoSuchDestinationFromAreaError(AreaError): pass

class area:
	"""a class modeling a street area on the board"""

	def __init__(self, name=''):
		self.name = name
		self.adjLocs = {}
		self.adjAreas ={}

	def addLocation(self, l):
		"""add a location to the list of adjcent locations"""
		self.adjLocs[l.name] = l

	def addArea(self, a):
		"""add a street area to the list of adjacent street areas"""
		self.adjAreas[a.name] = a

	def reachables(self, steps):
		"""returns the names of the locations and the street areas
		reachable from this area with <steps> movement points"""
		result = []
		result.append(self.name)
		if steps > 0:
			for k, v in self.adjLocs.iteritems():
				result.append(k)
			for k, v in self.adjAreas.iteritems():
				temp = v.reachables(steps-1)
				for n in temp:
					if n not in result:
						result.append(n)
		return result

	def distanceTo(self, dest):
		"""returns distance from this area to <dest>, raises 
		NoSuchDestinationFromAreaError if <dest> is not found on the board"""
		maxReachables = 0
		i = 0
		while True:
			r = self.reachables(i)
			if dest in r:
				return i
			if len(r) == maxReachables:
				raise NoSuchDestinationFromAreaError, "No place called %s exists on the board" % dest
			maxReachables = len(r)
			i = i + 1

