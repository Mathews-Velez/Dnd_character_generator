import random 
import Class_files.Weapons as Weapons
import Class_files.Equipment_packs as Equipment_packs
def Bard(x):
    
    #Print breif description
    print('\n\nYour class\n\nBard\n -A true jack of all trades; a bard can cover great amounts of ground when speaking about what they are able to do. A performer at heart, an inspiration to its allies, but above all a foul-mouthed to its foes. With its great charisma, his/her voice becomes its greatest weapon.')
    #Print Class Features
    print('For stat priority, Charisma followed by dexterity')
    
    #Hit points
    #Hit Dice: 
    print('Hit Dice\n -d8')
    #Hit Points at 1st Level:
    print('Hit points at Level 1\n 8 + Constitution_mod')
    #Hit Points at Higher Levels:
    print('Hit Points at Higher Levels: 1d8(or 5) + your constitution modifier per barbarian level after 1st')
     
    #Proficiencies
    print('\nProficiencies')
    #Armor: 
    print('-Armour:\n -Light armor')
    #Weapons:
    print('-Weapons:\n -Simple weapons, Handcrossbows, longswords, rapiers, shortswords')
    #Tools: 
    print('-Tools:\n -Three musical instruments of your choice')
    #Saving Throws: 
    print('-Saving Throws:\n -Dexterity, Charisma')
    
    #Skills
    skills = ('Acrobatics','Animal Handling','Arcana','Athletics','Deception','History','Insight','Intimidation','Investigation','Medicine','Nature','Perception','Performance','Persuassion','Religion','Sleight of Hand','Stealth','Survival')
    #fetching 2 unique strings from the tuple skills
    chosen_skills = random.sample(skills,2)
    print(f'Skills:\n -{chosen_skills}')
    
    #equipment
    print('\nEquipment')
    #weapons
    print('-Weapons')
    #first choice weapon
    first_choice = random.choice([1,3])
    if first_choice == 1:
        weapon,damage = Weapons.martial_melee_weapon('Rapier')
    elif first_choice == 2:
        weapon,damage= Weapons.martial_melee_weapon('Longsword')
    elif first_choice == 3:
        weapon,damage = Weapons.simple_melee_weapon()
    print(f'  Primary weapon {weapon,damage}')
    #second weapon choice 
    second_choice = random.choice([1,3])
    if second_choice == 1:
        weapon, damage = Weapons.simple_melee_weapon('Handaxe')
    else:
        weapon, damage = Weapons.simple_melee_weapon()
    print(f'  Secondary weapon{weapon,damage}')
    #equipment pack
    print('-equipment pack')
    Thrid_choice = random.choice([1,2])
    if Thrid_choice == 1:
        equipment_pack = Equipment_packs.equipment_pack('Diplomats_pack')
    if Thrid_choice == 2:
        equipment_pack = Equipment_packs.equipment_pack('Entertainers_pack')
    print(f'  {equipment_pack}')
    Fourth_choice = Weapons.simple_melee_weapon('Dagger')
    print(f'  Leather armour and a {Fourth_choice} ')