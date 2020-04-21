import Dice_roll_gen,random

def Aasimar(x): 
	
	#Male Names
	if x == 'Male':
		C_A_M_N= random.choice(['Aritian', 'Beltin', 'Cernan', 'Cronwier', 'Eran', 'Ilamin', 'Maudril', 'Okrin', 'Parant', 'Tural', 'Wyran', 'Zaigan'])
		print(f'Full name\n -{C_A_M_N}')
	
	#Female Names
	if x == 'Female':
		C_A_F_N= random.choice(['Arken', 'Arsinoe', 'Davina', 'Drinma', 'Imesah', 'Masozi','Nijena', 'Niramour', 'Ondrea', 'Rhialla', 'Valtyra'])
		print(f'Full name\n -{C_A_F_N}')
	
	#Asimar Traits 
	#Height
	if x == 'Male':
    		print(f'Height\n -{random.choice(range(5,8))}"{random.choice(range(1,13))}')
	if x == 'Female':
    		print(f'Height\n -{random.choice(range(4,7))}"{random.choice(range(1,13))}')
	#Age
	print(f'Age\n -{random.choice(range(12,160))}')
	#Skin tones	
	skin_color = random.choice(['Pale Brown','Dark Brown','Emerald','Gold','Silver'])
	print(f'Skin Color\n -{skin_color}')
	#Hair color 
	hair_color = random.choice(['Red','Blonde','Brown','Black','Silver'])
	print(f'Hair Color\n -{hair_color}')
	#Eye color
	eye_color = random.choice(['Pupil-less pale white','Gold','Grey','Topaz'])
	print(f'Eye Color\n -{eye_color}\nand 60ft Darkvision')
	
	
	#Aasimar Subraces
	C_Aasimar_subrace = random.choice(['Protector Aasimar', 'Scourge Aasimar','Fallen Aasimar'])
	print(f'Subrace\n -{C_Aasimar_subrace}\n\nStats for your adventurer\n')
	
	#Stat Rolls 
	#Fallen Aasimar Stats
	if C_Aasimar_subrace == 'Fallen Aasimar':
		Fallen_Aasimar_Stats = {'Strength:':Dice_roll_gen.roll_4_d6()+1, 'Dexterity:':Dice_roll_gen.roll_4_d6(),'Constitution:':Dice_roll_gen.roll_4_d6(),'Intelligence:':Dice_roll_gen.roll_4_d6(),'Wisdom:':Dice_roll_gen.roll_4_d6(),'Charisma:':Dice_roll_gen.roll_4_d6()+2}
		[print(f'{key}, {value},({(int((value-10)/2))})') for key, value in Fallen_Aasimar_Stats.items()]
	
	#Scourge Aasimar Stats
	if C_Aasimar_subrace == 'Scourge Aasimar':
		Scourge_Aasimar_Stats = {'Strength:':Dice_roll_gen.roll_4_d6(), 'Dexterity:':Dice_roll_gen.roll_4_d6(),'Constitution:':Dice_roll_gen.roll_4_d6()+1,'Intelligence:':Dice_roll_gen.roll_4_d6(),'Wisdom:':Dice_roll_gen.roll_4_d6(),'Charisma:':Dice_roll_gen.roll_4_d6()+2}
		[print(f'{key}, {value},({(int((value-10)/2))})') for key, value in Scourge_Aasimar_Stats.items()]
	
	#Protector Aasimar
	if C_Aasimar_subrace == 'Protector Aasimar':
		Protector_Aasimar_Stats = {'Strength:':Dice_roll_gen.roll_4_d6(), 'Dexterity:':Dice_roll_gen.roll_4_d6(),'Constitution:':Dice_roll_gen.roll_4_d6(),'Intelligence:':Dice_roll_gen.roll_4_d6(),'Wisdom:':Dice_roll_gen.roll_4_d6()+1,'Charisma:':Dice_roll_gen.roll_4_d6()+2}
		[print(f'{key}, {value},({(int((value-10)/2))})') for key, value in Protector_Aasimar_Stats.items()] 
