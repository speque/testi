class LocationError(Exception): pass
class NoSuchDestinationFromLocationError(LocationError): pass

class location:
	"""a class modeling a location on the board"""

	def __init__(self, name=''):
		self.name = name
		self.adjArea = None

	def reachables(self, steps):
		"""returns the names of the locations and the street areas
		reachable from this location with <steps> movement points"""
		result = []
		result.append(self.name)
		if steps > 0 and self.adjArea != None:
			r = self.adjArea.reachables(steps-1)
			for n in r:
				if n not in result:
					result.append(n)
		return result

	def distanceTo(self, dest):
		"""returns distance from this location to <dest>, raises 
		NoSuchDestinationFromLocationError if <dest> is not found on the board"""
		maxReachables = 0
		i = 0
		while True:
			r = self.reachables(i)
			if dest in r:
				return i
			if len(r) == maxReachables:
				raise NoSuchDestinationFromLocationError, "No place called %s exists on the board" % dest
			maxReachables = len(r)
			i = i + 1
