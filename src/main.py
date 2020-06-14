#random_npc_encounter_generator
import random, Races, Classes, Backgrounds

while True:

  print(' Welcome to Dungeon and Dragons Character Generator \n')

  race = random.choice(Races.race_list.keys())
  print(f'Race: {chosen_race}')

  class_ = random.choice(Classes.class_list.keys())
  print(f'Class: {class_}')

  background = random.choice(Background.background_list.keys())
  print(f'Background: {background}')

  gender = random.choice(["Male", "Female"])
  print(f'Gender: {gender}')

  Races.race_list[chosen_race](chosen_gender)# generate all info on the character's race
  Classes.class_list[chosen_class](chosen_race)# generate all the info on the characters class
  Backgrounds.background_list[chosen_background]()# generate all the info on the characters background

  #Exit Function
  try_again = input('\n\nTry again? (y/n): ')
  if try_again.lower()[0] == 'n':
    break
