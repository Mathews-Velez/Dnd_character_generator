import random, Races ,Classes, Backgrounds

while True:

  #random_npc_encounter_generator
  print(' Welcome to Dungeon and Dragons Character Generator \n')


  #Race Selector
  race_list = ('Human', 'Elf', 'Half_Orc', 'Dwarf', 'Tiefling', 'Dragonborn','Kenku','Goliath','Aasimar')
  chosen_race = random.choice(race_list)
  #chosen_race = 'Aasimar'
  print(f'Race\n -{chosen_race}')
  
  #Class selector
  character_class = ('Fighter', 'Ranger', 'Wizard', 'Bard', 'Barbarian', 'Rogue',
                     'Monk','Cleric','Druid','Paladin','Sorcerer','Warlock')
  chosen_class = random.choice(character_class)
  #chosen_class = 'Cleric'
  print(f'Class\n -{chosen_class}')
  
  #Backgrounds selector 
  background_list = ('Acolyte','Charlatan','Criminal')#('Sailor','Acolyte','Charlatan','Criminal','Entertainer','Hermit','Noble','Outlander','Sage','Soldier','Folk Hero','Urchin')
  chosen_background = random.choice(background_list)
  #chosen_background = 'Acolyte'
  print(f'Background\n -{chosen_background}')

  #Gender Selector
  gender_list = ('Male','Female')
  chosen_gender = random.choice(gender_list)
  print(f'Gender\n -{chosen_gender}') 

  #Prompts Races.py to generate all info on the characters race
  Races.race_list[chosen_race](chosen_gender)
  #Prompts Classes.py to generate all the info on the characters class
  Classes.class_list[chosen_class](chosen_race)
  #Prompts Backgrounds.py to generate all the info on the chracters background
  Backgrounds.background_list[chosen_background]()

  #Exit Function 
  try_again = input('\n\n Try again? (Press enter else n to stop)\n')
  if try_again.lower() == 'n':  
    exit()
