import random,Dice_roll_gen

#Dwarf race
def Dwarf(x):
	
	#Dwarf clan names
	Dwarf_clan_names = ('Balderk','Battlehammer','Brawnanvil','Dankil','Fireforge','Frostbeard','Gorunn','Holderhek','Ironfist','Loderr','Lotgehr','Rumnaheim')
	chosen_Dwarf_clan_name = random.choice(Dwarf_clan_names)
	
	#Dwarf male names
	if x == 'Male':
		D_m_full = ('Adrik','Alberich','Baern','Barendd','Brottor','Bruenor','Dain','Darrak','Morgran','Orsik','Rurik','Thorin','Travok')
		chosen_D_m_full = random.choice(D_m_full)
		print(f'Full name\n -{chosen_D_m_full}\nClan name\n -{chosen_Dwarf_clan_name}')
	
	#Dwarf female names
	if x == 'Female':
		D_f_full = ('Amber','Artin','Audhild','Bardryn','Dagnal','Diesa','Eldeth','Falkrunn','Finellen','Gunnloda','Helja','Torebera')
		chosen_D_f_full = random.choice(D_f_full)
		print(f'Full name\n -{chosen_D_f_full}\nClan name\n -{chosen_Dwarf_clan_name}')

	#Dwarf Traits
	#Age
	print(f'Age\n -{random.choice(range(30,350))}')
	#Skin color
	skin_color = random.choice(['Fair','Brown','Ash'])
	print(f'Skin color\n -{skin_color}')
	#Hair color
	hair_color = random.choice(['Black','Brown','Blond','Red'])
	print(f'Hair color\n -{hair_color}')
	#Eye color
	eye_color = random.choice(['Brown','Hazel','Green','Silver-blue'])
	print(f'Eye color\n -{eye_color}')
	#Height
	print(f'Height\n -{random.choice(range(4,6))},{random.choice(range(1,13))} your size is medium')


	#Dwarf Subraces
	Dwarf_Subraces = ('Hill Dwarf','Mountain Dwarf')
	C_Dwarf_Subraces = random.choice(Dwarf_Subraces)
	print(f'Subrace\n -{C_Dwarf_Subraces}\n\nStats for your adventurer (First int= Stat Second int= Modifier )\n') 
		
	#Stat Roll 
	#Hill Dwarf
	if C_Dwarf_Subraces == 'Hill Dwarf':
		Hill_Dwarf_Stats =  {'Strength:':Dice_roll_gen.roll_4_d6(), 'Dexterity:':Dice_roll_gen.roll_4_d6(),'Constitution:':Dice_roll_gen.roll_4_d6()+2,'Intelligence:':Dice_roll_gen.roll_4_d6(),'Wisdom:':Dice_roll_gen.roll_4_d6()+1,'Charisma:':Dice_roll_gen.roll_4_d6()}
		[print(f'{key}, {value},({(int((value-10)/2))})') for key, value in Hill_Dwarf_Stats.items()]
	#Moutain Dwarf
	if C_Dwarf_Subraces =='Mountain Dwarf':
		Mountain_Dwarf_Stats =  {'Strength:':Dice_roll_gen.roll_4_d6()+2, 'Dexterity:':Dice_roll_gen.roll_4_d6(),'Constitution:':Dice_roll_gen.roll_4_d6()+2,'Intelligence:':Dice_roll_gen.roll_4_d6(),'Wisdom:':Dice_roll_gen.roll_4_d6(),'Charisma:':Dice_roll_gen.roll_4_d6()}
		[print(f'{key}, {value},({(int((value-10)/2))})') for key, value in Mountain_Dwarf_Stats.items()]
