#random_npc_encounter_generator
import random

from dnd_character_generator import *
from dnd_character_generator import Alignments

#from Alignments import alignments  
#from Background import background_skill_profinciencies


def main():

	print(' \n\nWelcome to Dungeon and Dragons Character Generator \n')

	#randomly choose and print a gender
	gender = random.choice(["Male", "Female"])
	print(f'Gender: {gender}')

	#randomly choose and print a race from the keys in race_list located in Races.py
	race = random.choice(list(Races.race_list.keys()))
	print(f'Race: {race}')
	
	#randomly choose and print a class from the keys in class_list located in Classes.py
	class_ = random.choice(list(Classes.class_list.keys()))
	print(f'Class: {class_}')

	#randomly choose and print a background from the keys in background_list located in Backgrounds.py
	background = random.choice(list(Backgrounds.background_list.keys()))
	#background = 'Acolyte'
	print(f'Background: {background}')

	#Alignment
	alignment =random.choice(list(Alignments.alignments.keys()))
	alignment_description = Alignments.alignments[alignment]
	print(f'Alignment: {alignment}')
	

	#call the Races.py file accessing the dictionary race_list and calling the selected race method with gender as the argument
	Races.race_list[race](gender)

	#call Backgrounds.py file acess the backgrounds_skill_proficincies and get the selected value
	background_skills = Backgrounds.background_skill_profinciencies[background]
	
	#print chosen background with description
	print(f'\nYour alignment\n\n{alignment}\n')
	print(alignment_description)

	#calling the Races.py file accessing the dictionary race_list and calling the selected race method with background_skills as the argument for skill proficiencies overlap check
	Classes.class_list[class_](background_skills)
	
	# generate all the info on the characters background
	Backgrounds.background_list[background]()
	

if __name__ == "__main__":
	while True:
		main()

		#Exit Function
		#try_again = input('\n\nTry again? (y/n): ')
		#if try_again.lower()[0] == 'n':
		#	break
		try_again = input('\n\nTry again? (y/n): ')
		if try_again == 'n':
			break

