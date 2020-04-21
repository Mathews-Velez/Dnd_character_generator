import random,Dice_roll_gen

def Goliath(x): 
  
  #Nicknames
  G_N_N = ('Bearkiller','Dawncaller','Steadyhand','Twistedlimb','Wordpainterfearless','Flintfinder'
   'Horncarver','Keeneye','Lonehunter','Thread twisted', 'Twice-Orphaned', 'Longleaper')
  C_G_N_N = random.choice(G_N_N)  
  #Goliath clan names
  G_C_N = ('Anakalathai', 'Elanithino', 'Ogolakanu', 'Thuliaga', 'Thunukalathi', 'Katho-Olavi', 'Kolae-Giuliana',
   'Vaimei-Laga', 'Gathakanathi', 'Kalagiano')
  C_G_C_N = random.choice(G_C_N)  
  #Goliath names
  G_N = ('Aukan','Ilikan','Keothi','Kuori', 'Manner','Vaunea', 'Vimak','Maveith','Nalla','Orilo','Paavu','Pethani','Thalai','Thotham','Uthal' )
  C_G_N = random.choice(G_N)
  #Full Goliath name
  print(f'Full name\n -{C_G_N}\nNickname\n -{C_G_N_N}\nClan name\n -{C_G_C_N}')  
  
  #Goliath traits
  #Age
  print(f'Age\n -{random.choice(range(12,70))}')
  #Eye color
  eye_color = random.choice(['Blue','Green'])
  print(f'Eye color\n -{eye_color}')
  #Hair color
  if x == 'Male':
        print('Hair color\n -They are usually bald')
  if x == 'Female':
        print('Dark')
  #Size
  print(f'Size\n -{random.choice(range(6,9))}"{random.choice(range(1,13))}')
         
  #Stats Rolls
  print('\n\nStats for your adventurer\n')
  Goliath_Stats = {'Strength:':Dice_roll_gen.roll_4_d6()+2, 'Dexterity:':Dice_roll_gen.roll_4_d6(),'Constitution:':Dice_roll_gen.roll_4_d6()+1,'Intelligence:':Dice_roll_gen.roll_4_d6(),'Wisdom:':Dice_roll_gen.roll_4_d6()+1,'Charisma:':Dice_roll_gen.roll_4_d6()}
  [print(f'{key}, {value},({(int((value-10)/2))})') for key, value in Goliath_Stats.items()]