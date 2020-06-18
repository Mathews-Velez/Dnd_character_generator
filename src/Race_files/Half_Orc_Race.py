import Dice_roll_gen, random

def Half_Orc(gender):

	name_options = {
		"Male": ['Dench', 'Feng', 'Gell', 'Henk', 'Holg', 'Imsh', 'Keth', 'Krusk', 'Mhurren', 'Ront', 'Shump', 'Thokk'],
		"Female": ['Baggi', 'Emen', 'Engong', 'Kansif', 'Myev', 'Ovak', 'Ownka', 'Shautha', 'Sutha', 'Vola', 'Volan', 'Yevelda']
	}

	name = random.choice(name_options[gender])
	print(f'Full name: {name}')

	#Traits
	age = random.choice(range(12,70))
	print(f'Age: {age}')

	eye_color = 'Red'
	print(f'Eye Color: {eye_color} (is sometimes said to glow red)')

	hair_color = random.choice(['Black','Dark Brown','Dark red','Dark Grey'])
	print(f'Hair Color: {hair_color}')

	inches = random.choice(range(1,13))
	feet = random.choice(range(5,7))
	print(f"Height: {feet}\"{inches}, your size is medium")

	#Stats Rolls
	print('\n\nStats for your adventurer.\n[Stat]: [Value] ([Modifier])\n')
	half_orc_stats = {
		'Strength': Dice_roll_gen.roll_4_D6(2),
		'Dexterity': Dice_roll_gen.roll_4_D6(),
		'Constitution': Dice_roll_gen.roll_4_D6(1),
		'Intelligence': Dice_roll_gen.roll_4_D6(),
		'Wisdom': Dice_roll_gen.roll_4_D6(),
		'Charisma': Dice_roll_gen.roll_4_D6()
	}

	[print(f'{stat}: {data[0]} ({data[1]})') for stat, data in half_orc_stats.items()]

	# Created variables: gender, name, age, eye_color, hair_color, inches, feet, half_orc_stats
