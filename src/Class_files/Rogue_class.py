import random 
from dnd_character_generator.Class_files import Weapons
from dnd_character_generator.Class_files import Equipment_packs
def Rogue(reserved_skills):

	#Print breif description
	print('\n\nYour class\n\nRogue\n -Let’s get shady, grab a dagger and start stabbing. Rogues excel at sneaking around, scouting ahead, being dexterous and about everything you would expect a thief to be good at. In dungeons, they can help their party by deactivating traps or opening locked doors. Don’t expect them to wear much armor, nor be able to carry heavy stuff; but were your task to need some delicacy or swashbuckling, you’ve found the right person.')

	print('\nFor stat priority, Dexterity followed by Intelligence or Charisma\n')

	#Hit points
	print('Hit Dice\n -d8')
	print('Hit points at Level 1\n 8 + Constitution_mod')
	print('Hit Points at Higher Levels: 1d8(or 5) + your constitution modifier per Rogue level after 1st')

	#Proficiencies
	print('\nProficiencies')
	print('-Armour:\n -Light armour')
	print('-Weapons:\n -Simple weapons,Hand crossbow,Longswords,Rapiers, Shortswords')
	print("-Tools:\n -Theive's tools")
	print('-Saving Throws:\n -Dexterity, Intelligence')

	#Skills
	skills = ['Acrobatics','Athletics','Deception','Insight','Intimidation','Investigation','Perception','Performance','Persuassion','Sleight of hand','Stealth']
	#skill proficiencies overlap check
	for i in reserved_skills:
		if i in skills:
			skills.remove(i)

	chosen_skills = random.sample(skills,2)
	print(f'Skills:\n -{chosen_skills}')

	#equipment
	print('\nClass Equipment')

	#weapons
	print('-Weapons')

	#first choice weapon
	first_choice = random.choice([1,2])
	if first_choice == 1:
		weapon,damage = Weapons.martial_melee_weapon('Rapier')
	elif first_choice == 2:
		weapon,damage= Weapons.martial_melee_weapon('Shortsword')
	print(f'  Primary weapon {weapon,damage}')

	#second weapon choice
	second_choice = random.choice([1,2])
	if second_choice == 1:
		weapon, damage = Weapons.simple_ranged_weapon('Light Crossbow')
		print(f'  Secondary weapon{weapon,damage} with 20 arrows')
	elif second_choice == 2:
		weapon, damage = Weapons.martial_melee_weapon('Shortsword')
		print(f'  Secondary weapon{weapon,damage}')
	#third weapon choice
	weapon, damage = Weapons.simple_melee_weapon('Dagger')
	print(f'  Third weapon 2{weapon,damage}')

	#armor
	print('-Armor')
	print(' Leather armor')

	#equipment pack
	print('-Equipment pack')
	packs = random.choice([1,2,3])
	if packs == 1:
		equipment_pack = Equipment_packs.equipment_pack('Dungeoneers_pack')
	if packs == 2:
		equipment_pack = Equipment_packs.equipment_pack('Explorers_pack')
	if packs == 3:
		equipment_pack = Equipment_packs.equipment_pack('Burglars_pack')
	print(f'  {equipment_pack}')
