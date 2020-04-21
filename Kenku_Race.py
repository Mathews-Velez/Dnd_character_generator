import random, Dice_roll_gen
#Kenku
def Kenku(x):

    #Feather color
    feather_color = random.choice(['Dark brown','Jet black','Charcol black','Dark red'])
    print('Feather color\n -{feather_color}')
    #Eye color 
    print(f'Eye color\n -Black')
    #Height 
    print(f"Height\n -{random.choice(range(4,6))}'{random.choice(range(1,13))}, your size is small\n")
    #Stats rolls
    print('\nStats for your adventurer\n')
    Kenku_Stats = {'Strength:':Dice_roll_gen.roll_4_d6(), 'Dexterity:':Dice_roll_gen.roll_4_d6()+2,'Constitution:':Dice_roll_gen.roll_4_d6(),'Intelligence:':Dice_roll_gen.roll_4_d6(),'Wisdom:':Dice_roll_gen.roll_4_d6()+1,'Charisma:':Dice_roll_gen.roll_4_d6()}
    [print(f'{key}, {value},({(int((value-10)/2))})') for key, value in Kenku_Stats.items()]