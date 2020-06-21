import random
import Class_files.Weapons as Weapons
import Class_files.Equipment_packs as Equipment_packs

def Barbarian(gender):

	# brief description and features
	print('\n\nYour class\n\nBarbarian\n -Filled with their destructive rage and primal instincts, the barbarian is the class you choose if you want to be the meat shield in the front line dealing great amounts of damage. Who needs a shield when you can stand your foes’ puny attacks with your hardened skin and/or high evasiveness?')
	print('\nStat priority: Strength followed by Constitution.\n')

	# Hit Points
	print('Hit Dice\n -d12')
	print('Hit points at Level 1\n -12 + constitution modifier')
	print('Hit Points at Higher Levels:\n -roll 1d12(or 7) + your constitution modifier per barbarian level after 1st')

	#Proficiencies
	print('\nProficiencies:')
	print('-Armour:\n  -Light armor\n  -Medium armor\n  -Shields')
	print('-Weapons:\n  -Simple weapons\n  -Martial weapons')
	print('-Tools:\n  -None')
	print('-Saving Throws:\n  -Strength\n  -Constitution')

	#Skills
	skills = ('Animal Handling','Athletics','Intimidation','Nature','Perception','Survival')
	chosen_skills = random.sample(skills, 2)
	print(f'Skills:\n -{chosen_skills}')

	#equipment
	print('\nClass Equipment')

	#Weapons
	print('-Weapons:\n[weapon]:[Damage,Damage_type] ')
	#first choice weapon
	first_choice = random.choice([1,3])
	if first_choice == 1:
		weapon, damage = Weapons.martial_melee_weapon('Greataxe')
	else:
		weapon, damage = Weapons.martial_melee_weapon()
	print(f'  -Primary weapon: {weapon, damage}')
	#second weapon choice
	second_choice = random.choice([1,3])
	if second_choice == 1:
		s_weapon, s_damage = Weapons.simple_melee_weapon('Handaxe')
	else:
		s_weapon, s_damage = Weapons.simple_melee_weapon()
	print(f'  -Secondary weapon: {s_weapon, s_damage}')

	#equipment pack
	print('-Equipment pack')
	equipment_pack = Equipment_packs.equipment_pack('Explorers_pack')
	print(f'  -{equipment_pack}')
