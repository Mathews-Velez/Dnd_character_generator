import random
from dnd_character_generator import Dice_roll_gen

def Elf(gender):

	c_elf_family_name = random.choice(['Amakiir(Gemflower)', 'Amastacia(Starflower)', 'Galanodel(Moonwhisper)', 'Holimion(Diamonddew)', 'Ilphelkiir(Gemblossom)', 'Liadon(Silverfrond)', 'Miliamne(Oakenheel)', 'Nailo(Nightbreeze)', 'Siannodel(Moonbrook)', 'Xiloscient(Goldpetal)'])

	name_options = {
		"Male": ['Adran', 'Aelar', 'Aramil', 'Arannis', 'Aust', 'Berio', 'Berrian', 'Carric', 'Enialis', 'Heian', 'Ivellios', 'Laucian', 'Mindartis', 'Paelian', 'Quarian', 'Tharivol', 'Soveliss', 'Riardon'],
		"Female": ['Adire', 'Birel', 'Caelynn', 'Drusilia', 'Enna', 'Leshanna', 'Sariel', 'Vadannia', 'Naivara', 'Theirastra', 'Queleanna', 'Lia', 'Shava', 'Silaqui', 'Mialee', 'Jelenneth', 'Meriele']
	}

	name = random.choice(name_options[gender])
	print(f'First name: {name}\nFamily name: {c_elf_family_name}')

	#Traits
	age = random.choice(range(50,750))
	print(f'Age: {age}')

	eye_color = random.choice(['Blue','Violet','Green'])
	print(f'Eye Color: {eye_color}')

	hair_color = random.choice(['Dark brown','Autum Orange','Mossy Green','Deep Gold'])
	print(f'Hair Color: {hair_color}')

	inches = random.choice(range(1,13))
	feet = random.choice(range(5,7))
	print(f'Height: {feet}\"{inches}, your size is medium')


	#Subraces
	c_elf_subrace = random.choice([
		'High Elf',# +2 dexterity, +1 intelligence
		'Wood Elf',# +2 dexterity, +1 wisdom
		'Dark Elf'# +2 dexterity
	])
	print(f'Subrace: {c_elf_subrace}')

	#Stat Rolls
	print('\n\nStats for your adventurer.\n[Stat]: [Value] ([Modifier])\n')
	elf_stats = {
		'Strength': Dice_roll_gen.roll_4_D6(),
		'Dexterity': Dice_roll_gen.roll_4_D6(2),
		'Constitution': Dice_roll_gen.roll_4_D6(),
		'Intelligence': Dice_roll_gen.roll_4_D6(1 if c_elf_subrace == 'High Elf' else 0),
		'Wisdom': Dice_roll_gen.roll_4_D6(1 if c_elf_subrace == 'Wood Elf' else 0),
		'Charisma': Dice_roll_gen.roll_4_D6()
	}

	[print(f'{stat}: {data[0]} ({data[1]})') for stat, data in elf_stats.items()]

	# Created variables: gender, name, c_elf_family_name, age, eye_color, hair_color, inches, feet, c_elf_subrace, elf_stats
