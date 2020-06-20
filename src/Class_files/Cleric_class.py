import random 
import Class_files.Weapons as Weapons
import Class_files.Equipment_packs as Equipment_packs
def Cleric(x):

	#Print breif description
	print('\n\nYour class\n\nCleric\n -As well as with bards, clerics cover a wide amount of possibilities depending on the god you choose to follow. They are high spirited servants of their deities and follow their domains to choose a way of life. Both a warrior and spellcaster, they are able to cover practically any role in a party. Depending on their subclass, their Channel Divinity ability acts in different ways, granting direct powers from their gods.')
	
	print('\nFor stat priority, Wisdom followed by Strength or Constitution.\n')

	#Hit points
	print('Hit Dice\n -d8')
	print('Hit points at Level 1\n 8 + Constitution_mod')
	print('Hit Points at Higher Levels: roll 1d8(or 5) + your constitution modifier per Cleric level after 1st')

	#Proficiencies
	print('\nProficiencies')
	print('-Armour:\n -Light armor, medium armor, shields')
	print('-Weapons:\n -Simple weapons')
	print('-Tools:\n -None')
	print('-Saving Throws:\n -Wisdom, Charisma')

	#Skills
	skills = ('History','Insight','Medicine','Persuasion','Religion')
	chosen_skills = random.sample(skills,2)
	print(f'Skills:\n -{chosen_skills}')

	#equipment
	print('\nClass Equipment')

	#weapons
	print('-Weapons')
	#first choice weapon
	first_choice = random.choice([1,2])
	if first_choice == 1:
		weapon,damage = Weapons.simple_melee_weapon('Mace')
	elif first_choice == 2:
		weapon,damage= Weapons.martial_melee_weapon('Warhammer')
	print(f'  Primary weapon{weapon,damage}')

	#second weapon choice
	second_choice = random.choice(['Scale mail','Leather armor','Chain mail'])
	print(f'   Armour ({second_choice})')
	#Third choice
	Third_choice = random.choice([1,2])
	if Third_choice == 1:
		weapon, damage = Weapons.simple_ranged_weapon('Light Crossbow')
	elif Third_choice == 2:
		melee_or_range = random.choice(['melee','range'])
		if melee_or_range == 'melee':
			weapon,damage = Weapons.simple_melee_weapon()
		elif melee_or_range == 'range':
			weapon,damage = Weapons.simple_ranged_weapon()
	print(f'  Secondary weapon{weapon,damage}')
	
	#equipment pack
	print('-class equipment pack')
	equipment_choice = random.choice([1,2])
	if equipment_choice == 1:
		equipment_pack = Equipment_packs.equipment_pack('Explorers_pack')
	elif equipment_choice == 2:
		equipment_pack = Equipment_packs.equipment_pack('Priests_kit')
	print(f'  {equipment_pack}')
