import random 
import Class_files.Weapons as Weapons
import Class_files.Equipment_packs as Equipment_packs
def Monk(x):

	#Print breif description
	print('\n\nYour class\n\nMonk\n -Martial artists who can channel their Ki to do impressive feats as if they were magic users. No armor is necessary, just dexterity and the power of your mind. Deflect missiles thrown at you, changing the target to your enemies, move at the speed of the wind and fill your foes’ faces with a flurry blows.')
	#Print Class Features
	print('For stat priority, Dexterity followed by Wisdom and then Constitution')

	#Hit points
	#Hit Dice:
	print('Hit Dice\n -d8')
	#Hit Points at 1st Level:
	print('Hit points at Level 1\n 8 + Constitution_mod')
	#Hit Points at Higher Levels: 1d8 (or 5) + your constitution modifier per barbarian level after 1st
	print('Hit Points at Higher Levels: 1d8(or 5) + your constitution modifier per Fighter level after 1st')

	#Proficiencies
	print('\nProficiencies')
	#Weapons:
	print('-Weapons:\n -Simple weapons, Shortswords')
	#Tools: None
	print("-Tools:\n -Choose one type of artisan's tools or one musical instrument.")
	#Saving Throws:
	print('-Saving Throws:\n -Strength, Dexterity')

	#Skills
	skills = ('Acrobatics','Athletics','History','Insight','Religion','Stealth')
	#fetching 2 unique strings from the tuple skills
	chosen_skills = random.sample(skills,2)
	print(f'Skills:\n -{chosen_skills}')

	#equipment
	print('\nEquipment')
	#weapons
	print('-Weapons')

	#first choice weapon
	first_choice = random.choice([1,2])
	if first_choice == 1:
		weapon,damage = Weapons.martial_melee_weapon('Shortsword')
	elif first_choice == 2:
		weapon,damage= Weapons.simple_melee_weapon()
	print(f'  Primary weapon {weapon,damage}')
	#second weapon
	weapon, damage = Weapons.simple_ranged_weapon('Dart')
	print(f'  Secondary weapon 10{weapon,damage}')
	#equipment pack
	print('-Class Equipment Pack')
	Thrid_choice = random.choice([1,2])
	if Thrid_choice == 1:
		equipment_pack = Equipment_packs.equipment_pack('Dungeoneers_pack')
	if Thrid_choice == 2:
		equipment_pack = Equipment_packs.equipment_pack('Explorers_pack')
	print(f'  {equipment_pack}')
