class investigator:
	"""class modeling an investigator"""
	
	def __init__(self, name=''):
		self.name = name
		self.profession = ''
		self.maxStamina = 0
		self.stamina = 0
		self.maxSanity = 0
		self.sanity = 0
		self.focus = 0
		self.speedRow = []
		self.speed = 0
		self.sneakRow = []
		self.sneak = 0
		self.fightRow = []
		self.fight = 0
		self.willRow = []
		self.will = 0
		self.loreRow = []
		self.lore = 0
		self.luckRow = []
		self.luck = 0
		self.location = ''
		self.money = 0

	def modifyStamina(self, amount):
		"""Adds <amount> to investigator's stamina. Does not
		raise the stamina above current maximum stamina."""
		if self.stamina + amount <= self.maxStamina:
			self.stamina += amount
		else:
			self.stamina = self.maxStamina

        def modifySanity(self, amount):
		"""Adds <amount> to investigator's sanity. Does not
                raise the sanity above current maximum sanity."""
                if self.sanity + amount <= self.maxSanity:
                        self.sanity += amount
                else:
                        self.sanity = self.maxSanity

	def isConscious(self):
		"""Returns true if investigator's current stamina is 
		above zero, false otherwise."""
		if self.stamina > 0:
			return True
		else:
			return False

	def isSane(self):
                """Returns true if investigator's current sanity is 
                above zero, false otherwise."""
                if self.sanity > 0:
                        return True
                else:
                        return False
	
	def incrementSpeed(self):
		"""Increments speed by one step and decrements sneak by
		one step and lowers focus by one. Does not raise speed over maximum or 
		lower sneak below minimum."""
		if self.speedRow.index(self.speed) < 3:
			self.speed = self.speedRow[self.speedRow.index(self.speed) + 1]
			self.sneak = self.sneakRow[self.sneakRow.index(self.sneak) + 1]
			self.focus = self.focus -1

	def incrementSneak(self):
		"""Increments sneak by one step and decrements speed by
		one step and lowers focus by one. Does not raise sneak over maximum or 
		lower speed below minimum."""
		if self.sneakRow.index(self.sneak) > 0:
			self.speed = self.speedRow[self.speedRow.index(self.speed) - 1]
			self.sneak = self.sneakRow[self.sneakRow.index(self.sneak) - 1]
			self.focus = self.focus -1

	def incrementFight(self):
		"""Increments fight by one step and decrements will by
		one step and lowers focus by one. Does not raise fight over maximum or 
		lower will below minimum."""
		if self.fightRow.index(self.fight) < 3:
			self.fight = self.fightRow[self.fightRow.index(self.fight) + 1]
			self.will = self.willRow[self.willRow.index(self.will) + 1]
			self.focus = self.focus -1

	def incrementWill(self):
		"""Increments will by one step and decrements fight by
		one step and lowers focus by one. Does not raise will over maximum or 
		lower fight below minimum."""
		if self.willRow.index(self.will) > 0:
			self.fight = self.fightRow[self.fightRow.index(self.fight) - 1]
			self.will = self.willRow[self.willRow.index(self.will) - 1]
			self.focus = self.focus -1

	def incrementLore(self):
		"""Increments lore by one step and decrements luck by
		one step and lowers focus by one. Does not raise lore over maximum or 
		lower luck below minimum."""
		if self.loreRow.index(self.lore) < 3:
			self.lore = self.loreRow[self.loreRow.index(self.lore) + 1]
			self.luck = self.luckRow[self.luckRow.index(self.luck) + 1]
			self.focus = self.focus -1

	def incrementLuck(self):
		"""Increments luck by one step and decrements lore by
		one step and lowers focus by one. Does not raise luck over maximum or 
		lower lore below minimum."""
		if self.luckRow.index(self.luck) > 0:
			self.lore = self.loreRow[self.loreRow.index(self.lore) - 1]
			self.luck = self.luckRow[self.luckRow.index(self.luck) - 1]
			self.focus = self.focus -1

	def toString(self):
		result = 'Name: ' + self.name + '\nProfession: ' + self.profession \
		+ '\nStamina: %d\nSanity: %d\nFocus: %d\nLocation: %s\n' % (self.stamina, self.sanity, \
		self.focus, self.location)
		return result
