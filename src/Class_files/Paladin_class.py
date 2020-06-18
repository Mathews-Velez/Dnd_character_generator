import random 
import Class_files.Weapons as Weapons
import Class_files.Equipment_packs as Equipment_packs
def Paladin(x):

	#Print breif description
	print('\n\nYour class\n\nPaladin\n -A paladin is a person guided by an oath, their force of will and devotion so strong they are granted the ability to cast spells to smite their foes. They fight for justice and righteousness, with the idea of following their oath and ideals to the very end. For this, they use heavy armor to be front liners and protect their allies.')
	#Print Class Features
	print('For stat priority, Strength followed by Charisma')

	#Hit points
	#Hit Dice:
	print('Hit Dice\n -d10')
	#Hit Points at 1st Level:
	print('Hit points at Level 1\n 10 + Constitution_mod')
	#Hit Points at Higher Levels: 1d8 (or 5) + your constitution modifier per barbarian level after 1st
	print('Hit Points at Higher Levels: roll 1d10(or 6) + your constitution modifier per Paladin level after 1st')

	#Proficiencies
	print('\nProficiencies')
	#Armor:
	print('-Armour:\n -All armor and shields')
	#Weapons:
	print('-Weapons:\n -Simple weapons, Martial weapons')
	#Tools: None
	print('-Tools:\n -None')
	#Saving Throws:
	print('-Saving Throws:\n -Wisdom, Charisma')

	#Skills
	skills = ('Acrobatics','Animal Handling','Arcana','Athletics','Deception','History','Insight','Intimidation','Investigation','Medicine','Nature','Perception','Performance','Persuassion','Religion','Sleight of Hand','Stealth','Survival')
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
