import Dice_roll_gen, random

def Aasimar(gender):

	name_options = {
		"Male": ['Aritian', 'Beltin', 'Cernan', 'Cronwier', 'Eran', 'Ilamin', 'Maudril', 'Okrin', 'Parant', 'Tural', 'Wyran', 'Zaigan'],
		"Female": ['Arken', 'Arsinoe', 'Davina', 'Drinma', 'Imesah', 'Masozi','Nijena', 'Niramour', 'Ondrea', 'Rhialla', 'Valtyra']
	}

	name = random.choice(name_options[gender])
	print(f'Full name: {name}')

	#Traits
	#Height
	inches = random.choice(range(1,13))
	feet = random.choice(range(5,8))
	if gender == 'Female': feet -= 1# Female range was 4,7 just one less than male
	print(f'Height: {feet}\"{inches}')

	age = random.choice(range(12,160))
	print(f'Age: {age}')

	skin_color = random.choice(['Pale Brown','Dark Brown','Emerald','Gold','Silver'])
	print(f'Skin Color: {skin_color}')

	hair_color = random.choice(['Red','Blonde','Brown','Black','Silver'])
	print(f'Hair Color: {hair_color}')

	eye_color = random.choice(['Pupil-less pale white','Gold','Grey','Topaz'])
	print(f'Eye Color: {eye_color} and 60ft Darkvision')


	#Subraces
	c_aasimar_subrace = random.choice([
		'Protector Aasimar',# +1 widom, +2 charisma
		'Scourge Aasimar',# +1 constitution, +2 charisma
		'Fallen Aasimar'# +1 strength, +2 charisma
	])
	print(f'Subrace: {c_aasimar_subrace}')

	#Stat Rolls
	print('\n\nStats for your adventurer.\n[Stat]: [Value] ([Modifier])\n')
	aasimar_stats = {
		'Strength': Dice_roll_gen.roll_4_D6(1 if c_aasimar_subrace == 'Fallen Aasimar' else 0),
		'Dexterity': Dice_roll_gen.roll_4_D6(),
		'Constitution': Dice_roll_gen.roll_4_D6(1 if c_aasimar_subrace == 'Scourge Aasimar' else 0),
		'Intelligence': Dice_roll_gen.roll_4_D6(),
		'Wisdom': Dice_roll_gen.roll_4_D6(1 if c_aasimar_subrace == 'Protector Aasimar' else 0),
		'Charisma': Dice_roll_gen.roll_4_D6(2),# All three have a charisma bonus
	}

	[print(f'{stat}: {data[0]} ({data[1]})') for stat, data in aasimar_stats.items()]

	# Created variables: gender, name, inches, feet, age, skin_color, hair_color, eye_color, c_aasimar_subrace, aasimar_stats
