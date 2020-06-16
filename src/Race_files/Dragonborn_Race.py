import Dice_roll_gen, random

def Dragonborn(gender):

  chosen_dragonborn_clan_name = random.choice(['Clethinthiallor','Daardendrian','Delmirev','Drachedion','Fekenkabradon','Kepeshkmolik','Kerrhylon','Kimbatuul','Linxakasendalor','Myastan','Nemmonis','Norixius'])

  name_options = {
    "Male": ['Arjhan', 'Balasar', 'Bharash', 'Donaar', 'Ghesh', 'Heskan', 'Kriv', 'Medrash', 'Mehen', 'Nadarr', 'Pandjed', 'Patrin'],
    "Female": ['Akra','Biri','Daar','Farideh','Harann','Havilar','Jheri','Kava','Korinn','Mishann','Nala','Perra']
  }

  name = random.choice(name_options[gender])
  print(f'Full name: {name}\nClan name: {chosen_dragonborn_clan_name}')

  #Traits
  age = random.choice(range(12,80))
  print(f'Age: {age}')

  inches = random.choice(range(1,13))
  feet = random.choice(range(5,7))
  print(f"Height: {feet}\"{inches}, your size is medium")

  eye_color = random.choice(['Red','Gold'])
  print(f'Eye Color: {eye_color}')

  draconic_ancestries = {
    'Black': 'Acid',
    'Blue': 'Lightning',
    'Brass': 'Fire',
    'Bronze': 'Lightning',
    'Copper': 'Acid',
    'Gold': 'Fire',
    'Green': 'Poison',
    'Red': 'Fire',
    'Silver': 'Cold',
    'White': 'Cold'
  }
  dragon , damage_type  = random.choice(list(draconic_ancestries.items()))
  print(f'Dragon Species: {dragon}')
  print(f'Damage Type: {damage_type}')

  #Stat Rolls
  print('\n\nStats for your adventurer.\n[Stat]: [Value] ([Modifier])\n')
  dragonborn_stats = {
    'Strength': Dice_roll_gen.roll_4_D6(2),
    'Dexterity': Dice_roll_gen.roll_4_D6(),
    'Constitution': Dice_roll_gen.roll_4_D6(),
    'Intelligence': Dice_roll_gen.roll_4_D6(),
    'Wisdom': Dice_roll_gen.roll_4_D6(1),
    'Charisma': Dice_roll_gen.roll_4_D6(1)
  }

  [print(f'{stat}: {data[0]} ({data[1]})') for stat, data in dragonborn_stats.items()]

  # Created variables: gender, name, chosen_dragonborn_clan_name, age, inches, feet, eye_color, draconic_ancestries, dragon, damage_type, dragonborn_stats
