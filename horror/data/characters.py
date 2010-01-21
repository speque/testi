from horror.src.investigator import *

def veijo():
	i = investigator('Veijo Hietala')
	i.profession = 'Professor'
	i.maxStamina = 3
	i.stamina = 3
	i.maxSanity = 7
	i.sanity = 7
	i.focus = 2

	i.speedRow = [1, 2, 3, 4] 
	i.sneakRow = [5, 4, 3, 2]

	i.fightRow = [0, 1, 2, 3]
	i.willRow  = [5, 4, 3, 2]

	i.loreRow  = [3, 4, 5, 6]
	i.luckRow  = [4, 3, 2, 1]

	i.speed = i.speedRow[1]
	i.sneak = i.sneakRow[1]

	i.fight = i.fightRow[1]
	i.will  = i.willRow[1]

	i.lore  = i.loreRow[1]
	i.luck  = i.luckRow[1]

	i.location = 'Sirkkala'

	i.movement = i.speedRow[1]

	i.money = 2

	return i

