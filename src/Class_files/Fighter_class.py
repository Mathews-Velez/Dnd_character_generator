import random 
import Class_files.Weapons as Weapons
import Class_files.Equipment_packs as Equipment_packs
def Fighter(x):

	#Print breif description
	print('\n\nYour class\n\nFighter\n -What does a fighter do best? Well, fight of course. A really versatile class, as it can work in numerous ways. Add the fighting style and you can choose to have a one handed weapon accompanied by a shield, have a two handed weapon, two one handed ones (dual wielding), a ranged weapon and more! Once you’ve got that decided, ready yourself to start demolishing your foes, be it with your mighty strength or dexterous precision!')

	print('\nFor stat priority, Strength followed by dexterity and then Constitution\n')

	#Hit points
	print('Hit Dice\n -d10')
	print('Hit points at Level 1\n 10 + Constitution_mod')
	print('Hit Points at Higher Levels: roll 1d10(or 6) + your constitution modifier per Fighter level after 1st')

	#Proficiencies
	print('\nProficiencies')
	print('-Armour:\n -All armor and shields')
	print('-Weapons:\n -Simple weapons, Martial weapons')
	print('-Tools:\n -None')
	print('-Saving Throws:\n -Strength, Constitution')

	#Skills
	skills = ('Acrobatics','Animal Handling','Athletics','History','Insight','Intimidation','Perception','Survival')
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
	elif Thrid_choice == 2:
		equipment_pack = Equipment_packs.equipment_pack('Explorers_pack')
	print(f'  {equipment_pack}')
