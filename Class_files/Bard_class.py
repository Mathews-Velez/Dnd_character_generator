import random 
import Class_files.Weapons as Weapons
import Class_files.Equipment_packs as Equipment_packs
def Bard(x):
    
    #Print breif description
    print('\n\nYour class\n\nBard\n -The Bard is a master of song,speech, and the magic they contain. Bards say that the multiverse was spoken into existence, that the words of the gods gave it shape, and that echoes of these primordial Words of Creation still respond throughout the cosmos.')
    #Print Class Features
    print('For stat priority, Charisma followed by dexterity')
    
    #Hit points
    #Hit Dice: 1d12 per barbarian level
    print('Hit Dice\n -d8')
    #Hit Points at 1st Level: 8 + your Constitution modifier
    print('Hit points at Level 1\n 8 + Constitution_mod')
    #Hit Points at Higher Levels: 1d8 (or 5) + your constitution modifier per barbarian level after 1st
    print('Hit Points at Higher Levels: 1d8(or 5) + your constitution modifier per barbarian level after 1st')
     
    #Proficiencies
    print('\nProficiencies')
    #Armor: Light armor, medium armor, shields
    print('-Armour:\n -Light armor')
    #Weapons: Simple weapons, martial weapons
    print('-Weapons:\n -Simple weapons, Handcrossbows, longswords, rapiers, shortswords')
    #Tools: None
    print('-Tools:\n -Three musical instruments of your choice')
    #Saving Throws: Strength, Constitution
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