import random 
import Class_files.Weapons as Weapons
import Class_files.Equipment_packs as Equipment_packs
def Druid(x):

	#Print breif description
	print('\n\nYour class\n\nDruid\n -Preservers of balance and nature’s warriors, the druids aid their party members by using great support spells, as well as heavy damage dealing ones. They speak the language of the flora and fauna, as well as they can shapeshift into a wide amount of beasts for combat or situational purposes.')
	print('\nFor stat priority, Wisdom followed by Constitution.\n')

	#Hit points
	print('Hit Dice\n -d8')
	print('Hit points at Level 1\n 8 + Constitution_mod')
	print('Hit Points at Higher Levels: roll 1d8(or 5) + your constitution modifier per Druid level after 1st')

	#Proficiencies
	print('\nProficiencies')
	print('-Armour:\n -Light armor, medium armor, sheild,will not wear anything made of metal')
	print('-Weapons:\n -Clubs,Daggers,Darts,Javelins,Maces, Quarter staffs,Scimitars, Sickles, Slings, Spears')
	print('-Tools:\n -Herbalism kit')
	print('-Saving Throws:\n -Wisdom, Intelligence')

	#Skills
	skills = ('Arcana','Animal Handling','Insight','Medicine','Nature','Perception','Religion','Survival')
	chosen_skills = random.sample(skills,2)
	print(f'Skills:\n -{chosen_skills}')

	#equipment
	print('\nClass Equipment')
	
	#weapons
	print('-Weapons')
	#first choice weapon
	First_choice = random.choice([1,2,3])
	if First_choice == 1:
		weapon,damage = 'Wooden shield','+2ac'
	elif First_choice == 2:
		weapon,damage= Weapons.simple_melee_weapon()
	elif First_choice == 3:
		weapon,damage = Weapons.simple_ranged_weapon()
	print(f'  Primary weapon{weapon,damage}')

	#second weapon choice
	print('   Armour Leather armor')

	#Third choice
	Third_choice = random.choice([1,2])
	if Third_choice == 1:
		weapon, damage = Weapons.simple_melee_weapon()
	elif Third_choice == 2:
		weapon,damage = Weapons.martial_melee_weapon('Scimitar')
	print(f'  Secondary weapon{weapon,damage}')

	#equipment pack
	print('-equipment pack')
	equipment_pack = Equipment_packs.equipment_pack('Explorers_pack')
	print(f'  {equipment_pack}')
