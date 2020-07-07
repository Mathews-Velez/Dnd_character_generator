import random 
from dnd_character_generator.Class_files import Weapons
from dnd_character_generator.Class_files import Equipment_packs
def Warlock(x):

	#Print breif description
	print('\n\nYour class\n\nWarlock\n -Warlocks make pacts with extremely powerful beings, who don’t mind lending some power as they have so much they don’t even notice. However, it all comes with a price: There’s a reason this entity decided to accept the pact, and you might need to do some stuff to maintain the accord. Decide whether you want to have a big spellbook full of incantations, a strange summonable weapon or weird servants. Will you perish in the way to becoming an eldritch master?')
	#Print Class Features
	print('\nFor stat priority, Charisma followed by Wisdom and then Constitution\n')

	#Hit points
	#Hit Dice:
	print('Hit Dice\n -1d6 per sorcerer level')
	#Hit Points at 1st Level:
	print('Hit points at Level 1\n  6 + Constitution_mod')
	#Hit Points at Higher Levels:
	print('Hit Points at Higher Levels: 1d6(or 4)+ your constitution modifier per Warlock level after 1st')

	#Proficiencies
	print('\nProficiencies')
	#Armor:
	print('-Armour:\n -None')
	#Weapons:
	print('-Weapons:\n -Daggers, Darts, Slings, Quarterstaffs, Light Crossbows')
	#Tools: None
	print('-Tools:\n -None')
	#Saving Throws:
	print('-Saving Throws:\n -Constitution, Charisma')

	#Skills
	skills = ('Arcana','Deception','Insight','Intimidation','Persuassion','Religion','Religion')
	#fetching 2 unique strings from the tuple skills
	chosen_skills = random.sample(skills,2)
	print(f'Skills:\n -{chosen_skills}')

	#equipment
	print('\nClass Equipment')
	#weapons
	print('-Weapons')

	#first choice weapon
	first_choice = random.choice([1,2])
	if first_choice == 1:
		weapon,damage = Weapons.simple_ranged_weapon('Light Crossbow')
		print(f'  -Primary weapon: {weapon,damage}')
	elif first_choice == 2:
		r_or_m = random.choice(['r','m'])
		if r_or_m == 'r':
			weapon,damage = Weapons.simple_ranged_weapon()
		elif r_or_m == 'm':
			weapon,damage = Weapons.simple_melee_weapon()
		print(f'  Primary weapon {weapon,damage}')

	#second weapon choice
	second_choice = random.choice(['c','a'])
	if second_choice == 'c':
		spellcast_helper = 'a component pouch'
	elif second_choice =='a':
		spellcast_helper = 'an arcance focus'
	print(f'  Spellcasting helper: {spellcast_helper}')

	#equipment pack
	print('-equipment pack')
	Thrid_choice = random.choice([1,2])
	if Thrid_choice == 1:
		equipment_pack = Equipment_packs.equipment_pack('Dungeoneers_pack')
	if Thrid_choice == 2:
		equipment_pack = Equipment_packs.equipment_pack('Explorers_pack')
	print(f'  {equipment_pack}')
