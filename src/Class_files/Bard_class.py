import random
from dnd_character_generator.Class_files import Weapons
from dnd_character_generator.Class_files import Equipment_packs
def Bard(x):

	#Print breif description
	print('\n\nYour class\n\nBard\n -A true jack of all trades; a bard can cover great amounts of ground when speaking about what they are able to do. A performer at heart, an inspiration to its allies, but above all a foul-mouthed to its foes. With its great charisma, his/her voice becomes its greatest weapon.')
	#Print Class Features
	print('\nFor stat priority, Charisma followed by dexterity\n')

	#Hit points
	print('Hit Dice\n -d8')
	print('Hit points at Level 1\n 8 + Constitution_mod')
	print('Hit Points at Higher Levels: roll 1d8(or 5) + your constitution modifier per barbarian level after 1st')

	#Proficiencies
	print('\nProficiencies')
	print('-Armour:\n -Light armor')
	print('-Weapons:\n -Simple weapons, Handcrossbows, longswords, rapiers, shortswords')
	print('-Tools:\n -Three musical instruments of your choice')
	print('-Saving Throws:\n -Dexterity, Charisma')

	#Skills
	skills = ('Acrobatics','Animal Handling','Arcana','Athletics','Deception','History','Insight','Intimidation','Investigation','Medicine','Nature','Perception','Performance','Persuassion','Religion','Sleight of Hand','Stealth','Survival')
	chosen_skills = random.sample(skills,2)
	print(f'Skills:\n -{chosen_skills}')

	#equipment
	print('\nClass Equipment')

	#weapons
	print('-Weapons')
	#first choice weapon
	first_choice = random.choice([1,3])
	if first_choice == 1:
		weapon,damage = Weapons.martial_melee_weapon('Rapier')
	elif first_choice == 2:
		weapon,damage= Weapons.martial_melee_weapon('Longsword')
	elif first_choice == 3:
		weapon,damage = Weapons.simple_melee_weapon()
	print(f'  Primary weapon {weapon,damage}')
	#second weapon choice
	second_choice = random.choice([1,3])
	if second_choice == 1:
		weapon, damage = Weapons.simple_melee_weapon('Handaxe')
	else:
		weapon, damage = Weapons.simple_melee_weapon()
	print(f'  Secondary weapon{weapon,damage}')

	Fourth_choice = Weapons.simple_melee_weapon('Dagger')
	print(f'  Leather armour and a {Fourth_choice} ')

	#equipment pack
	print('-equipment pack')
	e_pack = random.choice(['Diplomats_pack','Entertainers_pack'])
	if e_pack == 'Diplomats_pack':
		equipment_pack = Equipment_packs.equipment_pack(e_pack)
	elif e_pack == 'Entertainers_pack':
		equipment_pack = Equipment_packs.equipment_pack(e_pack)
	print(f'  {e_pack}:{equipment_pack}')

