# coding=utf8
from horror.src.area import *
from horror.src.location import *
from horror.src.board import *

def turkuboard():
	"""returns the board of Turku"""

	"""Kartta:

	Student Village	
	  |
	  |
	Riverside -- University Campus
	  |
	  |
	Harbor
	"""

	campus = area('University Campus')
	hill = location('University Hill')
	hill.adjArea = campus
	park = location('Science Park')
	park.adjArea = campus
	sirkkala = location('Sirkkala')
	sirkkala.adjArea = campus
	campus.addLocation(hill)
	campus.addLocation(park)
	campus.addLocation(sirkkala)

	harbor = area('Harbor')
	castle = location('Turku Castle')
	castle.adjArea = harbor
	docks = location('Cargo Docks')
	docks.adjArea = harbor
	terminals = location('Cruiser Terminals')
	terminals.adjArea = harbor
	harbor.addLocation(castle)
	harbor.addLocation(docks)
	harbor.addLocation(terminals)

	river = area('Riverside')
	market = location('Old Marketsquare')
	market.adjArea = river
	church = location('Doom Church')
	church.adjArea = river
	fori = location('Föri the Ferry')
	fori.adjArea = river
	river.addLocation(market)
	river.addLocation(church)
	river.addLocation(fori)
	
	joukkila = area('Student Village')
	caribia = location('Caribia Hotel')
	caribia.adjArea = joukkila
	graveyard = location('Graveyard')
	graveyard.adjArea = joukkila
	pub = location('Pub Three Beers')
	pub.adjArea = joukkila 
	joukkila.addLocation(caribia)
	joukkila.addLocation(graveyard)
	joukkila.addLocation(pub)

	joukkila.addArea(river)
	river.addArea(joukkila)
	river.addArea(campus)
	river.addArea(harbor)
	campus.addArea(river)
	harbor.addArea(river)

	b = board()

	b.streets = {campus.name:campus, harbor.name:harbor, river.name:river, joukkila.name:joukkila}

	b.locs = {hill.name:hill, park.name:park, sirkkala.name:park, \
	castle.name:castle, docks.name:docks, terminals.name:terminals, \
	market.name:market, church.name:church, fori.name:fori, \
	caribia.name:caribia, graveyard.name:graveyard, pub.name:pub}
	
	return b
