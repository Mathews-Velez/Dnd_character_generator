import random
import Dice_roll_gen
#name
def Human(x):
  #human last name
  H_last_N = ('Gilliam', 'Wohlwend', 'Liss', 'Crume', ' Yepez', 'Crosland',
            ' Mcgraw', 'Lenard', 'Shreffler', 'Buchwald', 'Matte', 'Mccary',
            'Lowenstein', 'Fretz', 'Widrick', 'Dearborn', 'Brawley', 'Fuhrman')
  chosen_H_last = random.choice(H_last_N)
  #Human male first name
  if x == 'Male':
    H_m_first = ('Douglas', 'Mauro', 'Malcolm', 'Lucius', 'Shayne ','Preston',
             'Leon', 'Cyrus', 'Roberto', 'Barney', 'Clinton', 'Hubert',
             'Alonzo', 'Raphael', 'Bruce', 'Jed', 'Derick', 'Carmen')
    chosen_H_m_first = random.choice(H_m_first)
    #human male full name 
    chosen_human_full_name_male = (f'{chosen_H_m_first},{chosen_H_last}')
    print(f'Full name\n -{chosen_human_full_name_male}')
  
  #Human Female Full Name
  if x == 'Female':
    H_f_first = ('Bee', 'Janae', 'Carolin', 'Jacquie', 'Yanira', 'Britta', 'Ethel',
             'Alise', 'Rosaline', 'Shay', 'Claudia', 'Caroyln', 'Pansy ', 'Yi',
             'Tula', 'Saturnina', 'Branda', 'Oralee', 'Breanne', 'Julietta')
    chosen_H_f_first = random.choice(H_f_first)
    #human female full name 
    chosen_human_full_name_female = (f'{chosen_H_f_first},{chosen_H_last}')
    print(f'Full name\n -{chosen_human_full_name_female}')

  #Human Traits 
  #Age
  print(f'Age\n -{random.choice(range(12,70))}')
  #Eye Color
  eye_color = random.choice(['Amber','Brown','Hazel','Green','Blue','Gray'])
  print(f'Eye color\n -{eye_color}')
  #Hair 
  hair_color = random.choice(['Black','Gray','Platinum','White', 'Dark Blonde','Blonde','Bleach Blonde', 'Redhead','Light Redhead','Brunette','Aubun'])
  print(f'Hair color\n -{hair_color}')
  #Height  
  print(f"Height\n -{random.choice(range(5,7))}'{random.choice(range(1,13))}, your size is medium\n")
    
  #Stats rolls
  print('Stats for your adventurer (First int= Stat Second int= Modifier )\n')
  Human_Stats = {'Strength:':Dice_roll_gen.roll_4_d6()+1, 'Dexterity:':Dice_roll_gen.roll_4_d6()+1,'Constitution:':Dice_roll_gen.roll_4_d6()+1,'Intelligence:':Dice_roll_gen.roll_4_d6()+1,'Wisdom:':Dice_roll_gen.roll_4_d6()+1,'Charisma:':Dice_roll_gen.roll_4_d6()+1}
  [print(f'{key}, {value},({(int((value-10)/2))})') for key, value in Human_Stats.items()]
