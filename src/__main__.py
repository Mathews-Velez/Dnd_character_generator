#random_npc_encounter_generator
import random
from dnd_character_generator import *

def main():

	print(' \n\nWelcome to Dungeon and Dragons Character Generator \n')

	#randomly choose and print a race from the keys in race_list located in Races.py
	race = random.choice(list(Races.race_list.keys()))
	print(f'Race: {race}')
	
	#randomly choose and print a class from the keys in class_list located in Classes.py
	class_ = random.choice(list(Classes.class_list.keys()))
	print(f'Class: {class_}')

	#randomly choose and print a background from the keys in background_list located in Backgrounds.py
	background = random.choice(list(Backgrounds.background_list.keys()))
	print(f'Background: {background}')

	#randomly choose and print a gender
	gender = random.choice(["Male", "Female"])
	print(f'Gender: {gender}')
	
	Races.race_list[race](gender)# generate all info on the character's race
	Classes.class_list[class_](race)# generate all the info on the characters class
	Backgrounds.background_list[background]()# generate all the info on the characters background

if __name__ == "__main__":
	while True:
		main()

		#Exit Function
		try_again = input('\n\nTry again? (y/n): ')
		if try_again.lower()[0] == 'n':
			break
