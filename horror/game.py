# coding=utf8
from horror.src.area import *
from horror.src.location import *
from horror.src.investigator import *
from horror.src.board import *
from horror.src import skillcheck
from horror.data import characters
from horror.data import logo
from horror.data import map
from horror.data import turkuboard
import random
import curses
import traceback
import string
import locale

def thegame(stdscr):
	"""method for running the game"""
	b = turkuboard.turkuboard()
	veijo = characters.veijo()

	for s in logo.logo():
		stdscr.addstr(s, curses.A_BOLD)
	stdscr.addstr('\n                         Press any key to continue', curses.A_DIM)
	stdscr.refresh()
	stdscr.getkey()

	while True: 

		while True:

			stdscr.clear()

			# upkeep phase
			stdscr.addstr('TURKU HORROR\n\n', curses.A_BOLD)
			
			stdscr.addstr('Character:\n')
			stdscr.addstr(veijo.toString())

			stdscr.addstr('\nThis is the upkeep phase. Do you want to...\n\n')

			mainkeys = string.lowercase[:4]
			mainchoices = ['See the map', 'Adjust your skills', 'Continue for the next phase', \
			'Quit Turku Horror']

			for i, k in enumerate(mainkeys):
				c = '%s: %s \n' % (k, mainchoices[i])
				stdscr.addstr(c)
			stdscr.refresh()

			mainkey = stdscr.getkey()

			if mainkey in mainkeys:
				if mainkey == 'a': #show map
					stdscr.clear()
					for s in map.map():
						stdscr.addstr(s)
					stdscr.addstr('\nPress any key to return to menu')
					stdscr.refresh()
					stdscr.getkey()

				if mainkey == 'b': #adjust skills
					while True:
						stdscr.clear()
						if veijo.focus <= 0:
							stdscr.addstr('You have no more focus points left.\n')
							stdscr.addstr('Press any key to return to main menu.')
							stdscr.getkey()
							break
						else:
							stdscr.addstr('Speed: %s %s\n' % (veijo.speed, veijo.speedRow))
							stdscr.addstr('Sneak: %s %s\n' % (veijo.sneak, veijo.sneakRow))
							stdscr.addstr('Fight: %s %s\n' % (veijo.fight, veijo.fightRow))
							stdscr.addstr('Will:  %s %s\n' % (veijo.will, veijo.willRow))
							stdscr.addstr('Lore:  %s %s\n' % (veijo.lore, veijo.loreRow))
							stdscr.addstr('Luck:  %s %s\n' % (veijo.luck, veijo.luckRow))

							keys = string.lowercase[:7]
							choices = ['Increment speed', 'Increment sneak', \
							'Increment fight', 'Increment will', 'Increment lore', \
							'Increment luck', 'Return to main menu']
							stdscr.addstr('\nYou have %d focus point left. Do you want to...\n\n' % veijo.focus)
							for i, k in enumerate(keys):
								c = '%s: %s \n' % (k, choices[i])
								stdscr.addstr(c)

							key = stdscr.getkey()
							if key in keys:
								if key == 'a':
									veijo.incrementSpeed()
								if key == 'b':
									veijo.incrementSneak()
								if key == 'c':
									veijo.incrementFight()
								if key == 'd':
									veijo.incrementWill()
								if key == 'e':
									veijo.incrementLore()
								if key == 'f':
									veijo.incrementLuck()
								if key == 'g':
									break
				if mainkey == 'c':
					break

				if mainkey == 'd':
					return
			
		while True:
			stdscr.clear()

			# move phase
			stdscr.addstr('TURKU HORROR\n\n', curses.A_BOLD)
			
			stdscr.addstr('Character:\n')
			stdscr.addstr(veijo.toString())

			stdscr.addstr('\nThis is the move phase. Do you want to...\n\n')
			
			mainkeys = string.lowercase[:4]
			mainchoices = ['See the map', 'Move', 'Continue for the next phase', 'Quit Turku Horror']

			for i, k in enumerate(mainkeys):
				c = '%s: %s \n' % (k, mainchoices[i])
				stdscr.addstr(c)
			stdscr.refresh()

			mainkey = stdscr.getkey()
			if mainkey == 'a': #show map
				stdscr.clear()
				for s in map.map():
					stdscr.addstr(s)
				stdscr.addstr('\nPress any key to return to menu')
				stdscr.refresh()
				stdscr.getkey()

			if mainkey == 'b': #move
				stdscr.clear()
				stdscr.addstr('Your current location is %s.\n' % veijo.location)
				stdscr.addstr('You have %d movement points. Where do you want to move to?\n\n' % veijo.movement)
					
				r = []
				if veijo.location in b.locs:
					r = b.locs[veijo.location].reachables(veijo.movement)
				else:
					r = b.streets[veijo.location].reachables(veijo.movement)

				keys = string.lowercase[:len(r)]

				for i, k in enumerate(keys):
					if i == 0:
						c = '%s: %s (stay here)\n' % (k, r[i])
					else:
						c = '%s: %s \n' % (k, r[i])
					stdscr.addstr(c)
					
				key = stdscr.getkey()
				current = veijo.location
				veijo.location = r[keys.index(key)]
				if current != veijo.location:
					if current in b.locs:
						veijo.movement = veijo.movement - b.locs[current].distanceTo(veijo.location)
					else:
						veijo.movement = veijo.movement - b.streets[current].distanceTo(veijo.location)

			if mainkey == 'c':
				break

			if mainkey == 'd':
				return
		
		stdscr.clear()

		if veijo.location in b.locs:
			stdscr.addstr('TURKU HORROR\n\n', curses.A_BOLD)
			
			stdscr.addstr('Character:\n')
			stdscr.addstr(veijo.toString())

			skills = ['speed', 'sneak', 'fight', 'will', 'lore', 'luck']
			skillvalues = [veijo.speed, veijo.sneak, veijo.fight, veijo.will, veijo.lore, veijo.luck]
			modifiers = [0, -1, -1, -1, -2, -2, -3]
			difficulties = [1, 1, 1, 1, 1, 1, 2, 2, 3]
			betTypes = ['stamina', 'sanity']
			rewards = [1, 1, 1, 2, 2, 3]
			penalties = [1, 1, 2, 2, 3, 3]
			
			skill = random.choice(skills)
			modifier = random.choice(modifiers)
			difficulty = random.choice(difficulties)
			rewardType = random.choice(betTypes)
			reward = random.choice(rewards)
			penaltyType = random.choice(betTypes)
			penalty = random.choice(penalties)

			stdscr.addstr('\nThere is a voluntary challenge in %s.\n\n' % veijo.location)
			stdscr.addstr('Make a %s (%d) [%d] check.\n' % (skill, modifier, difficulty))
			stdscr.addstr('If you pass, gain %d %s.\n' % (reward, rewardType))
			stdscr.addstr('If you fail, lose %d %s.\n\n' % (penalty, penaltyType))
			stdscr.addstr('Your %s is currently %d. Do you want to try?\n\n' % (skill, skillvalues[skills.index(skill)]))

			mainkeys = string.lowercase[:2]
			mainchoices = ['Yes', 'No']

			for i, k in enumerate(mainkeys):
				c = '%s: %s \n' % (k, mainchoices[i])
				stdscr.addstr(c)
			stdscr.refresh()

			while True:
				mainkey = stdscr.getkey()
				if mainkey in mainkeys:
					break

			if mainkey == 'a':
				s = skillcheck.doSkillCheck(skillvalues[skills.index(skill)], modifier, difficulty)
				if s.succeeded:
					stdscr.addstr('Success! (Your throw was %s) You gain %d %s.\n' % (str(s.throw), reward, rewardType))
					if rewardType == 'stamina':
						veijo.modifyStamina(reward)
					else:
						veijo.modifySanity(reward)
				else:
					stdscr.addstr('Failure! (Your throw was %s) You lose %d %s.\n' % (str(s.throw), penalty, penaltyType))
					if penaltyType == 'stamina':
						veijo.modifyStamina(-penalty)
					else:
						veijo.modifySanity(-penalty)

				if not veijo.isConscious() or not veijo.isSane():
					if not veijo.isConscious():
						stdscr.addstr('\nYou have gone unconscious and can not continue.')
					else:
						stdscr.addstr('\nYou have gone insane and can not continue.')
					stdscr.addstr('\nPress any key to end the game.')
					stdscr.getkey()
					return
				else:
					stdscr.addstr('\nPress any key to continue.')
					stdscr.getkey()

if __name__=='__main__':
	"""initialises and starts the game """
	# Curses wrapper by Andrew Kuchling 
	# See http://gnosis.cx/publish/programming/charming_python_6.html
	try:
		# Initialize curses
		stdscr=curses.initscr()
		# Turn off echoing of keys, and enter cbreak mode,
		# where no buffering is performed on keyboard input
		curses.noecho()
		curses.cbreak()
		# In keypad mode, escape sequences for special keys
		# (like the cursor keys) will be interpreted and
		# a special value like curses.KEY_LEFT will be returned
		stdscr.keypad(1)

		thegame(stdscr) # Enter the main program

		# Set everything back to normal
		stdscr.keypad(0)
		curses.echo()
		curses.nocbreak()
		curses.endwin() # Terminate curses
	except:
		# In event of error, restore terminal to sane state.
		stdscr.keypad(0)
		curses.echo()
		curses.nocbreak()
		curses.endwin()
		traceback.print_exc() # Print the exception
