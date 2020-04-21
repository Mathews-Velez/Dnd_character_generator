import random,Dice_roll_gen
def Elf(x):    
	
	#Family Names
	C_Elf_Family_Name =random.choice(['Amakiir(Gemflower)','Amastacia(Starflower)','Galanodel(Moonwhisper)','Holimion(Diamonddew)','Ilphelkiir(Gemblossom)','Liadon(Silverfrond)','Miliamne(Oakenheel)','Nailo(Nightbreeze)','Siannodel(Moonbrook)','Xiloscient(Goldpetal)'])
	#Elf Male Names
	if x == 'Male':
	 chosen_E_m_first = random.choice(['Adran', 'Aelar', 'Aramil', 'Arannis', 'Aust', 'Berio', 'Berrian',
	          'Carric', 'Enialis', 'Heian', 'Ivellios', 'Laucian', 'Mindartis',
	          'Paelian', 'Quarian', 'Tharivol', 'Soveliss', 'Riardon'])
	 print(f'First name\n -{chosen_E_m_first}\nFamily name\n -{C_Elf_Family_Name}') 
	#Elf Female Names
	if x == 'Female':
	  chosen_E_f_first = random.choice(['Adire', 'Birel', 'Caelynn', 'Drusilia', 'Enna', 'Leshanna',
	          'Sariel', 'Vadannia', 'Naivara', 'Theirastra', 'Queleanna', 'Lia',
	          'Shava', 'Silaqui', 'Mialee', 'Jelenneth', 'Meriele'])
	  print(f'First name\n -{chosen_E_f_first}\nFamily name\n -{C_Elf_Family_Name}')

	#Elf traits
	#Age
	print(f'Age\n -{random.choice(range(50,750))}')
	#Eye Color
	eye_color = random.choice(['Blue','Violet','Green'])
	print(f'Eye color\n -{eye_color}')
	#Hair color
	hair_color = random.choice(['Dark brown','Autum Orange','Mossy Green','Deep Gold'])
	print(f'Hair color\n -{hair_color}')
	#Size
	print(f"Height\n -{random.choice(range(5,7))}'{random.choice(range(1,13))}, your size is medium")
	#Elf Subraces
	C_Elf_Subrace =random.choice(['High Elf','Wood Elf','Dark Elf'])
	print(f'Elf Subrace\n -{C_Elf_Subrace}\n\nStats for your adventurer\n')



	#Stat Rolls
	#High Elf Stats
	if C_Elf_Subrace == 'High Elf':
		High_Elf_Stats = {'Strength:':Dice_roll_gen.roll_4_d6(), 'Dexterity:':Dice_roll_gen.roll_4_d6()+2,'Constitution:':Dice_roll_gen.roll_4_d6(),'Intelligence:':Dice_roll_gen.roll_4_d6()+1,'Wisdom:':Dice_roll_gen.roll_4_d6(),'Charisma:':Dice_roll_gen.roll_4_d6()}
		[[print(f'{key}, {value},({(int((value-10)/2))})') for key, value in High_Elf_Stats.items()]]
	
	#Wood Elf Stats
	if C_Elf_Subrace == 'Wood Elf':
		Wood_Elf_Stats = {'Strength:':Dice_roll_gen.roll_4_d6(), 'Dexterity:':Dice_roll_gen.roll_4_d6()+2,'Constitution:':Dice_roll_gen.roll_4_d6(),'Intelligence:':Dice_roll_gen.roll_4_d6(),'Wisdom:':Dice_roll_gen.roll_4_d6()+1,'Charisma:':Dice_roll_gen.roll_4_d6()}
		[[print(f'{key}, {value},({(int((value-10)/2))})') for key, value in Wood_Elf_Stats.items()]]
	
	#Dark Elf Aasimar
	if C_Elf_Subrace == 'Dark Elf':
		Dark_Elf_Stats = {'Strength:':Dice_roll_gen.roll_4_d6(), 'Dexterity:':Dice_roll_gen.roll_4_d6()+2,'Constitution:':Dice_roll_gen.roll_4_d6(),'Intelligence:':Dice_roll_gen.roll_4_d6(),'Wisdom:':Dice_roll_gen.roll_4_d6(),'Charisma:':Dice_roll_gen.roll_4_d6()}
		[[print(f'{key}, {value},({(int((value-10)/2))})') for key, value in Dark_Elf_Stats.items()]] 
