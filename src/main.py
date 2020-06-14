#random_npc_encounter_generator
import random, Races, Classes, Backgrounds

while True:

  print(' Welcome to Dungeon and Dragons Character Generator \n')

  race = random.choice(list(Races.race_list.keys()))
  print(f'Race: {race}')

  class_ = random.choice(list(Classes.class_list.keys()))
  print(f'Class: {class_}')

  background = random.choice(list(Backgrounds.background_list.keys()))
  print(f'Background: {background}')

  gender = random.choice(["Male", "Female"])
  print(f'Gender: {gender}')

  Races.race_list[race](gender)# generate all info on the character's race
  Classes.class_list[class_](race)# generate all the info on the characters class
  Backgrounds.background_list[background]()# generate all the info on the characters background

  #Exit Function
  try_again = input('\n\nTry again? (y/n): ')
  if try_again.lower()[0] == 'n':
    break
