import Dice_roll_gen, random

def Kenku(gender):

	# Traits
	feather_color = random.choice(['Dark brown','Jet black','Charcol black','Dark red'])
	print(f'Feather Color: {feather_color}')

	eye_color = 'Black'
	print(f'Eye color: {eye_color}')

	inches = random.choice(range(1,13))
	feet = random.choice(range(4,6))
	print(f"Height: {feet}\"{inches}, your size is small\n")

	#Stats rolls
	print('\n\nStats for your adventurer.\n[Stat]: [Value] ([Modifier])\n')
	kenku_stats = {
		'Strength': Dice_roll_gen.roll_4_D6(),
		'Dexterity': Dice_roll_gen.roll_4_D6(2),
		'Constitution': Dice_roll_gen.roll_4_D6(),
		'Intelligence': Dice_roll_gen.roll_4_D6(),
		'Wisdom': Dice_roll_gen.roll_4_D6(1),
		'Charisma': Dice_roll_gen.roll_4_D6()
	}

	[print(f'{stat}: {data[0]} ({data[1]})') for stat, data in kenku_stats.items()]

	# Created variables: gender, feather_color, eye_color, inches, feet, kenku_stats
