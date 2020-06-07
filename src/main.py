#random_npc_encounter_generator
import random, Races, Classes, Backgrounds

while True:

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
  print(f'Class\n -{chosen_class}')

  #Backgrounds selector
  background_list = ('Acolyte','Charlatan','Criminal')#('Sailor','Acolyte','Charlatan','Criminal','Entertainer','Hermit','Noble','Outlander','Sage','Soldier','Folk Hero','Urchin')
  chosen_background = random.choice(background_list)
  print(f'Background\n -{chosen_background}')

  #Gender Selector
  gender_list = ('Male','Female')
  chosen_gender = random.choice(gender_list)
  print(f'Gender\n -{chosen_gender}')

  Races.race_list[chosen_race](chosen_gender)# generate all info on the character's race
  Classes.class_list[chosen_class](chosen_race)# generate all the info on the characters class
  Backgrounds.background_list[chosen_background]()# generate all the info on the characters background

  #Exit Function
  try_again = input('\n\nTry again? (y/n): ')
  if try_again.lower()[0] == 'n':
    break