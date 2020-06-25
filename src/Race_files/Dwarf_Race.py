import random
from dnd_character_generator import Dice_roll_gen

def Dwarf(gender):

	chosen_dwarf_clan_name = random.choice(['Balderk', 'Battlehammer', 'Brawnanvil', 'Dankil', 'Fireforge', 'Frostbeard', 'Gorunn', 'Holderhek', 'Ironfist', 'Loderr', 'Lotgehr', 'Rumnaheim'])

	name_options = {
		"Male": ['Adrik', 'Alberich', 'Baern', 'Barendd', 'Brottor', 'Bruenor', 'Dain', 'Darrak', 'Morgran', 'Orsik', 'Rurik', 'Thorin', 'Travok'],
		"Female": ['Amber', 'Artin', 'Audhild', 'Bardryn', 'Dagnal', 'Diesa', 'Eldeth', 'Falkrunn', 'Finellen', 'Gunnloda', 'Helja', 'Torebera']
	}

	name = random.choice(name_options[gender])
	print(f'Full name: {name}\nClan name: {chosen_dwarf_clan_name}')

	#Traits
	age = random.choice(range(30, 350))
	print(f'Age: {age}')

	skin_color = random.choice(['Fair','Brown','Ash'])
	print(f'Skin Color: {skin_color}')

	hair_color = random.choice(['Black','Brown','Blond','Red'])
	print(f'Hair Color: {hair_color}')

	eye_color = random.choice(['Brown','Hazel','Green','Silver-blue'])
	print(f'Eye Color: {eye_color}')

	inches = random.choice(range(1, 13))
	feet = random.choice(range(4, 6))
	print(f'Height: {feet}\"{inches}, your size is medium')


	#Subraces
	c_dwarf_subrace = random.choice([
		'Hill Dwarf',# +2 constitution, +1 wisdom
		'Mountain Dwarf'# +2 strength, +2 constitution
	])
	print(f'Subrace: {c_dwarf_subrace}')

	#Stat Rolls
	print('\n\nStats for your adventurer.\n[Stat]: [Value] ([Modifier])\n')
	dwarf_stats = {
		'Strength': Dice_roll_gen.roll_4_D6(2 if c_dwarf_subrace == 'Mountain Dwarf' else 0),
		'Dexterity': Dice_roll_gen.roll_4_D6(),
		'Constitution': Dice_roll_gen.roll_4_D6(2),
		'Intelligence': Dice_roll_gen.roll_4_D6(),
		'Wisdom': Dice_roll_gen.roll_4_D6(1 if c_dwarf_subrace == 'Hill Dwarf' else 0),
		'Charisma': Dice_roll_gen.roll_4_D6()
	}

	[print(f'{stat}: {data[0]} ({data[1]})') for stat, data in dwarf_stats.items()]

	# Created variables: gender, name, chosen_dwarf_clan_name, age, skin_color, hair_color, eye_color, inches, feet, c_dwarf_subrace, dwarf_stats
