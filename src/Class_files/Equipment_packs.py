#Equipment packs 
def equipment_pack (x):
	Burglars_pack = ('a backpack','a bag of 1000 ball bearings','10 feet of string','a bell','5 candles','a crowbar','a hammer','10 pitons','a hooded lantern','2 flasks of oil','5 days of rations','a tinderbox','a water skin','50 feet of hempen rope')

	Diplomats_pack = ('a chest','2 cases for maps and scrolls','a set of fine clothes','a bottle of ink','an ink pen','a lamp','2 flasks of oil','5 sheets of paper','a vial of perfume','sealing wax','soap')

	Dungeoneers_pack = ('a backpack','a crowbar','a hammer','10 pitons','10 torches','a tinderbox', '10 days of rations','a waterskin','50 feet of hempen rope')

	Entertainers_pack = ('a backpack','a bedroll','2 costumes','5 candles','5 days of rations','a waterskin','a disguise kit')

	Explorers_pack = ('a backpack','a bedroll','a mess kit','a tinderbox','10 torches','10 days of rations','a waterskin','50 feet of hempen rope')

	Priests_kit = ('a backpack','a blanket','10 candles','a tinderbox','an alms box','2 blocks of insence','a censer','vestments','2 days of rations','a waterskin')

	Scholars_pack = ('a backpack','a book of lore','a bottle of ink','an ink pen','10 sheets of parchment','a small bag of sand','a small knife')

    #assign each tuple to the name as a string in a dictionary
	#outputting pack selected
	if x == 'Burglars_pack':
		return Burglars_pack
	elif x == 'Diplomats_pack':
		return Diplomats_pack
	elif x == 'Dungeoneers_pack':
		return Dungeoneers_pack
	elif x == 'Entertainers_pack':
		return Entertainers_pack
	elif x == 'Explorers_pack':
		return Explorers_pack
	elif x == 'Priests_kit':
		return Priests_kit
	elif x == 'Scholars_pack':
		return Scholars_pack
	else:
		print('Error invalid input')
