import random 
from dnd_character_generator.Class_files import Weapons
from dnd_character_generator.Class_files import Equipment_packs
def Sorcerer(x):

	#Print breif description
	print('\n\nYour class\n\nSorcerer\n -Due to some random or pre-established occurrence, magic runs through you. This means you can “cheat” in a certain way to be able to use magic at will, instead of having to learn how to cast it. Sorcerers are also equipped with a pool of magic they get their sorcery points from, letting them twist spells to their will in different ways.')
	#Print Class Features
	print('\nFor stat priority, Charisma followed by Constitution\n')

	#Hit points
	print('Hit Dice\n -d6')
	print('Hit points at Level 1\n 6 + Constitution_mod')
	print('Hit Points at Higher Levels: 1d6(or 4) + your constitution modifier per Sorcerer level after 1st')

	#Proficiencies
	print('\nProficiencies')
	print('-Armour:\n -None')
	print('-Weapons:\n -Daggers, Darts, Slings, Quarterstaffs, Light crossbow')
	print('-Tools:\n -None')
	print('-Saving Throws:\n -Charisma, Constitution')

	#Skills
	skills = ('Arcana','Deception','Intimidation','Persuasion','Religion')
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
		print(f'  Primary weapon{weapon,damage} and 20 bolts')
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
		print(f'  Dungeoneers pack:{equipment_pack}')

	elif Thrid_choice == 2:
		equipment_pack = Equipment_packs.equipment_pack('Explorers_pack')
		weapon,damage = Weapons.simple_melee_weapon('Dagger')
		print(f'  Explorers pack:{equipment_pack} and 2{weapon,damage}')
