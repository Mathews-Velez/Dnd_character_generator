import random 
import Class_files.Weapons as Weapons
import Class_files.Equipment_packs as Equipment_packs
def Ranger(x):

	#Print breif description
	print('\n\nYour class\n\nRanger\n -')
	#Print Class Features
	print('For stat priority, ')

	#Hit points
	#Hit Dice:
	print('Hit Dice\n -')
	#Hit Points at 1st Level:
	print('Hit points at Level 1\n  + Constitution_mod')
	#Hit Points at Higher Levels:
	print('Hit Points at Higher Levels:  + your constitution modifier per Ranger level after 1st')

	#Proficiencies
	print('\nProficiencies')
	#Armor:
	print('-Armour:\n -All armor and shields')
	#Weapons:
	print('-Weapons:\n -Simple weapons, Martial weapons')
	#Tools: None
	print('-Tools:\n -None')
	#Saving Throws:
	print('-Saving Throws:\n -Strength, Constitution')

	#Skills
	skills = ('')
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
		weapon,damage = Weapons.martial_melee_weapon()
	elif first_choice == 2:
		weapon,damage= Weapons.martial_melee_weapon()

	print(f'  Primary weapon {weapon,damage}')

	#second weapon choice
	second_choice = random.choice([1,2])
	if second_choice == 1:
		weapon, damage = Weapons.simple_ranged_weapon('Light Crossbow')
	elif second_choice == 2:
		weapon, damage = Weapons.simple_melee_weapon('Handaxe')
	print(f'  Secondary weapon{weapon,damage}')

	#equipment pack
	print('-equipment pack')
	Thrid_choice = random.choice([1,2])
	if Thrid_choice == 1:
		equipment_pack = Equipment_packs.equipment_pack('Dungeoneers_pack')
	if Thrid_choice == 2:
		equipment_pack = Equipment_packs.equipment_pack('Explorers_pack')
	print(f'  {equipment_pack}')
