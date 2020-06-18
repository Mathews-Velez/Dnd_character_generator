import Dice_roll_gen, random

def Human(gender):

	last_name = random.choice(['Gilliam', 'Wohlwend', 'Liss', 'Crume', ' Yepez', 'Crosland', 'Mcgraw', 'Lenard', 'Shreffler', 'Buchwald', 'Matte', 'Mccary', 'Lowenstein', 'Fretz', 'Widrick', 'Dearborn', 'Brawley', 'Fuhrman'])
	name_options = {
		"Male": ['Douglas', 'Mauro', 'Malcolm', 'Lucius', 'Shayne ','Preston', 'Leon', 'Cyrus', 'Roberto', 'Barney', 'Clinton', 'Hubert', 'Alonzo', 'Raphael', 'Bruce', 'Jed', 'Derick', 'Carmen'],
		"Female": ['Bee', 'Janae', 'Carolin', 'Jacquie', 'Yanira', 'Britta', 'Ethel', 'Alise', 'Rosaline', 'Shay', 'Claudia', 'Caroyln', 'Pansy ', 'Yi', 'Tula', 'Saturnina', 'Branda', 'Oralee', 'Breanne', 'Julietta']
	}

	name = random.choice(name_options[gender])
	print(f'Full name: {name} {last_name}')

	#Traits
	age = random.choice(range(12,70))
	print(f'Age: {age}')

	eye_color = random.choice(['Amber','Brown','Hazel','Green','Blue','Gray'])
	print(f'Eye Color: {eye_color}')

	hair_color = random.choice(['Black','Gray','Platinum','White', 'Dark Blonde','Blonde','Bleach Blonde', 'Redhead','Light Redhead','Brunette','Aubun'])
	print(f'Hair Color: {hair_color}')

	inches = random.choice(range(1,13))
	feet = random.choice(range(5,7))
	print(f"Height: {feet}\"{inches}, your size is medium")

	#Stats Rolls
	print('\n\nStats for your adventurer.\n[Stat]: [Value] ([Modifier])\n')
	human_stats = {
		'Strength': Dice_roll_gen.roll_4_D6(1),
		'Dexterity': Dice_roll_gen.roll_4_D6(1),
		'Constitution': Dice_roll_gen.roll_4_D6(1),
		'Intelligence': Dice_roll_gen.roll_4_D6(1),
		'Wisdom': Dice_roll_gen.roll_4_D6(1),
		'Charisma': Dice_roll_gen.roll_4_D6(1)
	}

	[print(f'{stat}: {data[0]} ({data[1]})') for stat, data in human_stats.items()]

	# Created variables: gender, name, last_name, age, eye_color, hair_color, inches, feet, human_stats
