import Dice_roll_gen, random

def Tiefling(gender):

  tiefling_virtue_name = random.choice(['Art', 'Carrion', 'Chant', 'Creed', 'Despair', 'Excellence', 'Fear', 'Glory', 'Hope', 'Ideal', 'Music', 'Nowhere'])

  name_options = {
    "Male": ['Akmenos', 'Amnon', 'Barakas', 'Damakos', 'Ekemon', 'Lados', 'Kairon', 'Leucis', 'Melech', 'Mordai', 'Morthos', 'Pelaios'],
    "Female": ['Akta', 'Anakis', 'Brysies', 'Criella', 'Damaia', 'Ea', 'Kallista', 'Lerissa', 'Makaria', 'Nemeia', 'Orianna', 'Pheleia']
  }

  name = random.choice(name_options[gender])
  print(f'Full name: {name}\nVirtue name: {tiefling_virtue_name}')

  #Traits
  age = random.choice(range(12,120))
  print(f'Age: {age}')

  eye_color = random.choice(['Black', 'gold', 'red', 'silver', 'Solid white'])
  print(f'Eye Color: {eye_color}')

  hair_color = random.choice(['Red', 'Brown', 'Black', 'Dark blue', 'Purple'])
  print(f'Hair Color: {hair_color}')

  inches = random.choice(range(1,13))
  feet = random.choice(range(5,7))
  print(f"Height: {feet}\"{inches}, your size is medium")

  #Stats Rolls
  print('\n\nStats for your adventurer.\n[Stat]: [Value] ([Modifier])\n')
  tiefling_stats = {
    'Strength': Dice_roll_gen.roll_4_D6(),
    'Dexterity': Dice_roll_gen.roll_4_D6(),
    'Constitution': Dice_roll_gen.roll_4_D6(),
    'Intelligence': Dice_roll_gen.roll_4_D6(1),
    'Wisdom': Dice_roll_gen.roll_4_D6(),
    'Charisma': Dice_roll_gen.roll_4_D6(2)
  }

  [print(f'{stat}: {data[0]} ({data[1]})') for stat, data in half_orc_stats.items()]

  # Created variables: gender, name, tiefling_virtue_name, age, eye_color, hair_color, inches, feet, tiefling_stats
