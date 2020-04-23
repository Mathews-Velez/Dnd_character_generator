import random, Races 

while True:

  #random_npc_encounter_generator
  print(' Welcome to Dungeon and Dragons Character Generator \n')
  
  #display


  #Race Selector
  race_list = ('Human', 'Elf', 'Half_Orc', 'Dwarf', 'Tiefling', 'Dragonborn','Kenku','Goliath','Aasimar')
  chosen_race = random.choice(race_list)
  #chosen_race = 'Aasimar'
  print(f'Race\n -{chosen_race}')
  
  #Class selector
  character_class = ('Fighter', 'Ranger', 'Wizard', 'Bard', 'Barbarian', 'Rogue',
                     'Monk','Cleric','Druid','Paladin','Sorcerer','Warlock')
  chosen_class = random.choice(character_class)
  print(f'Class\n -{chosen_class}')
   #Class Subclass
  

  #Backgrounds selector 
  background_list = ('Criminal','Sailor','Acolyte','Charlatan','City Watch','Criminal','Entertainer','Fisher','Gambler','Hermit','Noble','Outlander','Sage','Smuggler','Soldier'
  ,'Bounty Hunter','Folk Hero')
  chosen_background = random.choice(background_list)
  print(f'Background\n -{chosen_background}')

  #Gender Selector
  gender_list = ('Male','Female')
  chosen_gender = random.choice(gender_list)
  print(f'Gender\n -{chosen_gender}') 

  #Prompts Races.py to generate all info on the characters race
  Races.race_list[chosen_race](chosen_gender)

  #Protmpt user to ask if they would like more details on their characters background

  #Exit Function 
  try_again = input('\n\n Try again? (Press enter else n to stop)\n')
  if try_again.lower() == 'n':  
    exit()