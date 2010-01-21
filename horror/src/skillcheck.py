import random

def throw(skill, modifier):
	"""throws <skill>+<modifier> dices and returns 
	the result as a list"""
	
	result = []
	for i in range(skill + modifier):
		result.append(random.randint(1, 6))

	return result

def check(difficulty, throw):
	"""returns true if the lis in <throw> contains at least
	<difficulty> 5s or 6s"""

	successes = 0
	for v in throw:
		if v == 5 or v == 6:
			successes = successes + 1
	if successes >= difficulty:
		return True
	else:
		return False

def doSkillCheck(skill, modifier, difficulty=1):
	"""performs a skill check with skill level <skill>,
	modified by <modifier> and with difficulty level 
	<difficulty>"""

	t = throw(skill, modifier)
	s = check(difficulty, t)
	return skillCheckResult(s, t)

class skillCheckResult:
	"""contains infromation of a performed skill check"""
	
	def __init__(self, succeeded, throw):
		self.succeeded = succeeded
		self.throw = throw

