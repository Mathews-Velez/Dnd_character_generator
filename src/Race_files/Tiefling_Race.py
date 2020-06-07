import random,Dice_roll_gen
  
def Tiefling(x):
  #Tiefling virtue names
  Tiefling_virtue_names = ('Art','Carrion','Chant','Creed','Despair','Excellence','Fear','Glory','Hope','Ideal','Music','Nowhere')
  chosen_Tiefling_virtue_name = random.choice(Tiefling_virtue_names)
  
  #Tiefling male names
  if x == 'Male':
    T_m_full = ('Akmenos','Amnon','Barakas','Damakos','Ekemon','Lados','Kairon','Leucis','Melech','Mordai','Morthos','Pelaios')
    chosen_T_m_full = random.choice(T_m_full)
    print(f'Full name\n -{chosen_T_m_full}\nVirtue name\n -{chosen_Tiefling_virtue_name}')
  
  #Tiefling female names
  if x == 'Female':
    T_f_full = ('Akta','Anakis','Brysies','Criella','Damaia','Ea','Kallista','Lerissa','Makaria','Nemeia','Orianna','Pheleia')
    chosen_T_f_full = random.choice(T_f_full)
    print(f'Full name\n -{chosen_T_f_full}\nVirtue name\n -{chosen_Tiefling_virtue_name}')

  #Tiefling Traits 
  #Age 
  print(f'Age\n -{random.choice(range(12,120))}')
  #Eye color
  eye_color = random.choice(['Black', 'gold', 'red', 'silver', 'Solid white'])
  print(f'Eye color\n -{eye_color}')
  #Hair color
  hair_color = random.choice(['Red', 'Brown', 'Black', 'Dark blue', 'Purple'])
  print(f'Hair color\n -{hair_color}')
  #Height 
  print(f"Height\n -{random.choice(range(5,7))}'{random.choice(range(1,13))}, your size is medium\n")

  #Stats rolls
  print('\nStats for your adventurer (First int= Stat Second int= Modifier )\n')
  Tiefling_Stats = {'Strength:':Dice_roll_gen.roll_4_d6(), 'Dexterity:':Dice_roll_gen.roll_4_d6(),'Constitution:':Dice_roll_gen.roll_4_d6(),'Intelligence:':Dice_roll_gen.roll_4_d6()+1,'Wisdom:':Dice_roll_gen.roll_4_d6(),'Charisma:':Dice_roll_gen.roll_4_d6()+2}
  [print(f'{key}, {value},({(int((value-10)/2))})') for key, value in Tiefling_Stats.items()]
