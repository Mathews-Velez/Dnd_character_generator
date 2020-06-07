import random,Dice_roll_gen
def Half_Orc(x):  
  #Half Orc Male Names
  if x == 'Male':
    O_m_full = ('Dench','Feng','Gell','Henk','Holg','Imsh','Keth','Krusk','Mhurren','Ront','Shump','Thokk')
    chosen_O_m_full = random.choice(O_m_full)
    print(f'Full name\n -{chosen_O_m_full}')
  
  #Half Orc Female Names
  if x == 'Female':
    O_f_full = ('Baggi','Emen','Engong','Kansif','Myev','Ovak','Ownka','Shautha','Sutha','Vola','Volan','Yevelda')
    chosen_O_f_full = random.choice(O_f_full)
    print(f'Full name\n -{chosen_O_f_full}')   

  #Half Orc Traits 
  #Age
  print(f'Age\n -{random.choice(range(12,70))}')
  #Eye Color
  print(f'Eye color\n -Red(sometimes is said to glow red)')
  #Hair 
  hair_color = random.choice(['Black','Dark Brown','Dark red','Dark Grey'])
  print(f'Hair color\n -{hair_color}')
  #Height
  print(f"Height\n -{random.choice(range(5,7))}'{random.choice(range(1,13))}, your size is medium\n")

  #Stats Rolls
  print('Stats for your adventurer (First int= Stat Second int= Modifier )\n')
  Half_Orc_Stats = {'Strength:':Dice_roll_gen.roll_4_d6()+2, 'Dexterity:':Dice_roll_gen.roll_4_d6(),'Constitution:':Dice_roll_gen.roll_4_d6()+1,'Intelligence:':Dice_roll_gen.roll_4_d6(),'Wisdom:':Dice_roll_gen.roll_4_d6(),'Charisma:':Dice_roll_gen.roll_4_d6()}
  [print(f'{key}, {value},({(int((value-10)/2))})') for key, value in Half_Orc_Stats.items()]