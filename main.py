import random, Races ,Classes

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
  chosen_class = 'Barbarian'
  print(f'Class\n -{chosen_class}')
   #Class Subclass
   

  #Backgrounds selector 
  background_list = ('Sailor','Acolyte','Charlatan','Criminal','Entertainer','Hermit','Noble','Outlander','Sage','Soldier','Folk Hero')
  chosen_background = random.choice(background_list)
  print(f'Background\n -{chosen_background}')

  #Gender Selector
  gender_list = ('Male','Female')
  chosen_gender = random.choice(gender_list)
  print(f'Gender\n -{chosen_gender}') 

  #Prompts Races.py to generate all info on the characters race
  Races.race_list[chosen_race](chosen_gender)
  Classes.class_list[chosen_class](chosen_race)
  

  #Exit Function 
  try_again = input('\n\n Try again? (Press enter else n to stop)\n')
  if try_again.lower() == 'n':  
    exit()
