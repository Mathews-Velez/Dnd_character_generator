#Equipment packs 
def equipment_pack (x):
	Burglars_pack = ('a backpack','a bag of 1000 ball bearings','10 feet of string','a bell','5 candles','a crowbar','a hammer','10 pitons','a hooded lantern','2 flasks of oil','5 days of rations','a tinderbox','a water skin','50 feet of hempen rope')

	Diplomats_pack = ('a chest','2 cases for maps and scrolls','a set of fine clothes','a bottle of ink','an ink pen','a lamp','2 flasks of oil','5 sheets of paper','a vial of perfume','sealing wax','soap')

	Dungeoneers_pack = ('a backpack','a crowbar','a hammer','10 pitons','10 torches','a tinderbox', '10 days of rations','a waterskin','50 feet of hempen rope')

	Entertainers_pack = ('a backpack','a bedroll','2 costumes','5 candles','5 days of rations','a waterskin','a disguise kit')

	Explorers_pack = ('a backpack','a bedroll','a mess kit','a tinderbox','10 torches','10 days of rations','a waterskin','50 feet of hempen rope')

	Priests_kit = ('a backpack','a blanket','10 candles','a tinderbox','an alms box','2 blocks of insence','a censer','vestments','2 days of rations','a waterskin')

	Scholars_pack = ('a backpack','a book of lore','a bottle of ink','an ink pen','10 sheets of parchment','a small bag of sand','a small knife')

    #Dictionary assingment of each equipmentPack and their title stringified
    packs= { 'Burglars_pack' : Burglars_pack, 'Diplomats_pack' : Diplomats_pack, 'Dungeoneers_pack' : Dungeoneers_pack, 'Entertainers_pack' : Entertainers_    pack, 'Explorers_pack' : Explorers_pack, 'Prists_kit' : Priests_kit, 'Scholars_pack' : Scholars_pack}
    #assign each tuple to the name as a string in a dictionary7
	#outputting pack selected
    return packs[x]
