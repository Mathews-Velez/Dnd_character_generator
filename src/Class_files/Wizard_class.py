import random 
from dnd_character_generator.Class_files import Weapons
from dnd_character_generator.Class_files import Equipment_packs
def Wizard(reserved_skills):

	#Print breif description
	print('\n\nYour class\n\nWizard\n -Wizards decide to go in adventures to further their knowledge. The great world in front of them has thousands of spells for you to learn and master. With a spellbook at hand, they will look for or buy them to become a greater spellcaster. Just transcribe them to the book and you’ll understand why wizards are such a versatile class. The amount of spells they can learn greatly surpasses all other classes’ lists.')
	
	print('For stat priority, ')

	#Hit points
	print('Hit Dice\n -d6')
	print('Hit points at Level 1\n  + Constitution_mod')
	print('Hit Points at Higher Levels: 1d(or ) + your constitution modifier per level after 1st')

	#Proficiencies
	print('\nProficiencies')
	print('-Armour:\n -None')
	print('-Weapons:\n -Daggers, Darts, Slings, Quarterstaff, Light crossbow ')
	print('-Tools:\n -None')
	print('-Saving Throws:\n -Intelligence, Wisdom ')

	#Skills
	skills = ['Arcana','History','Insight','Investigation','Medicine','Religion']
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
		weapon,damage = Weapons.simple_melee_weapon('Quarterstaff')
	elif first_choice == 2:
		weapon,damage= Weapons.simple_melee_weapon('Dagger')

	print(f'  Primary weapon {weapon,damage}')

	#second weapon choice
	second_choice = random.choice(['c','a'])
	if second_choice == 'c':
		spellcast_helper = 'a component pouch'
	elif second_choice =='a':
		spellcast_helper = 'an arcance focus'
	print(f'  Spellcasting helper: {spellcast_helper}')

	#equipment pack
	print('-Equipment pack')
	Thrid_choice = random.choice([1,2])
	if Thrid_choice == 1:
		equipment_pack = Equipment_packs.equipment_pack('Scholars_pack')
	if Thrid_choice == 2:
		equipment_pack = Equipment_packs.equipment_pack('Explorers_pack')
	print(f'  {equipment_pack} and a spellbook')
