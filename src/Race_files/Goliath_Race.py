import Dice_roll_gen, random

def Goliath(gender):

	nickname = random.choice(['Bearkiller', 'Dawncaller', 'Steadyhand', 'Twistedlimb', 'Wordpainterfearless', 'Flintfinder'
	 'Horncarver', 'Keeneye', 'Lonehunter', 'Thread twisted', 'Twice-Orphaned', 'Longleaper'])

	clan_name = random.choice(['Anakalathai', 'Elanithino', 'Ogolakanu', 'Thuliaga', 'Thunukalathi', 'Katho-Olavi', 'Kolae-Giuliana', 'Vaimei-Laga', 'Gathakanathi', 'Kalagiano'])

	name = random.choice(['Aukan', 'Ilikan', 'Keothi', 'Kuori', 'Manner', 'Vaunea', 'Vimak', 'Maveith', 'Nalla', 'Orilo', 'Paavu', 'Pethani', 'Thalai', 'Thotham', 'Uthal'])
	print(f'Full name: {name}\nNickname: {nickname}\nClan name: {clan_name}')

	#Traits
	age = random.choice(range(12,70))
	print(f'Age: {age}')

	eye_color = random.choice(['Blue','Green'])
	print(f'Eye Color: {eye_color}')

	hair_color = 'Dark' if gender == 'Female' else 'Bald'
	print(f'Hair Color: {hair_color}')

	inches = random.choice(range(1,13))
	feet = random.choice(range(6,9))
	print(f'Size: {feet}\"{inches}')

	#Stats Rolls
	print('\n\nStats for your adventurer.\n[Stat]: [Value] ([Modifier])\n')
	goliath_stats = {
		'Strength': Dice_roll_gen.roll_4_D6(2),
		'Dexterity': Dice_roll_gen.roll_4_D6(),
		'Constitution': Dice_roll_gen.roll_4_D6(1),
		'Intelligence': Dice_roll_gen.roll_4_D6(),
		'Wisdom': Dice_roll_gen.roll_4_D6(1),
		'Charisma': Dice_roll_gen.roll_4_D6()
	}

	[print(f'{stat}: {data[0]} ({data[1]})') for stat, data in goliath_stats.items()]

	# Created variables: gender, name, nickname, clan_name, age, eye_color, hair_color, inches, feet, goliath_stats
