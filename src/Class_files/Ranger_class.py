import random 
from dnd_character_generator.Class_files import Weapons
from dnd_character_generator.Class_files import Equipment_packs
def Ranger(x):

	#Class
	print('\n\nYour class\n\nRanger\n -A natural explorer seeking adventures, who on their way found a special hatred towards a certain beast or monster. Able to master any fighting style as long as they don’t involve heavy weapons or armor. Spellcasters by default, due to their connection with nature and/or the Feywild, they are excellent scouts and allies to have by your side.')

	print('\nFor stat priority, Dexterity followed by Wisdom\n')

	#Hit points
	print('Hit Dice\n -1d10')
	print('Hit points at Level 1\n 10 + Constitution_mod')
	print('Hit Points at Higher Levels: roll 1d10(or6) + your constitution modifier per Ranger level after 1st')

	#Proficiencies
	print('\nProficiencies')
	print('-Armour:\n -Light armor, Medium armor, Shields')
	print('-Weapons:\n -Simple weapons, Martial weapons')
	print('-Tools:\n -None')
	print('-Saving Throws:\n -Strength, Dexterity')

	#Skills
	skills = ('Animal handling','Athletics','Insight','Investigation','Nature','Perception','Stealth','Survival')
	chosen_skills = random.sample(skills,3)
	print(f'Skills:\n -{chosen_skills}')

	#Equipment
	print('\nClass Equipment')

	#Weapons
	print('-Weapons')
	#first choice weapon
	first_choice = random.choice([1,2])
	if first_choice == 1:
		weapon,damage = Weapons.martial_melee_weapon('Shortsword')
	elif first_choice == 2:
		weapon,damage= Weapons.martial_melee_weapon()
	print(f'  Primary weapon 2{weapon,damage}')

	#second weapon choice
	second_choice = random.choice([1,2])
	weapon, damage = Weapons.martial_ranged_weapon('Longbow')
	print(f'  Secondary weapon{weapon,damage}')

	#equipment pack
	print('-equipment pack')
	Thrid_choice = random.choice([1,2])
	if Thrid_choice == 1:
		equipment_pack = Equipment_packs.equipment_pack('Dungeoneers_pack')
	if Thrid_choice == 2:
		equipment_pack = Equipment_packs.equipment_pack('Explorers_pack')
	print(f'  {equipment_pack}')
