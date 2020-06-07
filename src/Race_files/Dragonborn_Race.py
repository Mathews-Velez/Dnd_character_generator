import random, Dice_roll_gen   

def Dragonborn(x):   
  
  #Dragonborn clan names
  chosen_Dragonborn_clan_name = random.choice(['Clethinthiallor','Daardendrian','Delmirev','Drachedion','Fekenkabradon','Kepeshkmolik','Kerrhylon','Kimbatuul','Linxakasendalor','Myastan','Nemmonis','Norixius'])
  
  #Dragonborn male names 
  if x == 'Male':
    chosen_D_m_full = random.choice(['Arjhan','Balasar','Bharash','Donaar','Ghesh','Heskan','Kriv','Medrash','Mehen','Nadarr','Pandjed','Patrin'])
    print(f'Full name\n -{chosen_D_m_full}\nClan name\n -{chosen_Dragonborn_clan_name}')
  
  #Dragonborn female names
  if x == 'Female':
    chosen_T_f_full = random.choice(['Akra','Biri','Daar','Farideh','Harann','Havilar','Jheri','Kava','Korinn','Mishann','Nala','Perra'])
    print(f'Full name\n -{chosen_T_f_full}\nClan name\n -{chosen_Dragonborn_clan_name}')
  
  #Dragonborn Traits
  #Age
  print(f'Age\n -{random.choice(range(12,80))}')
  #Size
  print(f"Height\n -{random.choice(range(5,7))}'{random.choice(range(1,13))}, your size is medium")
  #Eye color
  eye_color = random.choice(['Red','Gold'])
  print(f'Eye Color\n -{eye_color}')
  #Dragonborn Draconic Ancestry
  Draconic_Ancestries = {'Black' : 'Acid', 'Blue' :'Lightning','Brass':'Fire','Bronze':'Lightning','Copper':'Acid', 'Gold':'Fire', 'Green':'Poison','Red':'Fire','Silver':'Cold','White':'Cold'}
  Dragon , Damage_type  = random.choice(list(Draconic_Ancestries.items()))
  print(f'Dragon Species\n -{Dragon}')
  print(f'Damage Type\n -{Damage_type}\n\nStats for your adventurer (First int= Stat Second int= Modifier )\n')
 
  #Stat rolls
  Dragonborn_Stats = {'Strength:':Dice_roll_gen.roll_4_d6()+2, 'Dexterity:':Dice_roll_gen.roll_4_d6(),'Constitution:':Dice_roll_gen.roll_4_d6(),'Intelligence:':Dice_roll_gen.roll_4_d6(),'Wisdom:':Dice_roll_gen.roll_4_d6()+1,'Charisma:':Dice_roll_gen.roll_4_d6()+1}
  [print(f'{key}, {value},({(int((value-10)/2))})') for key, value in Dragonborn_Stats.items()]
  
  