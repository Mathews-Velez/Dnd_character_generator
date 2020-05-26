import random 
import Class_files.Weapons as Weapons
import Class_files.Equipment_packs as Equipment_packs
def Cleric(x):  
    
    #Print breif description
    print('\n\nYour class\n\nCleric\n -Clerics are conduits of divine magic, manifesting it as miraculous effects.The gods dont grant this power to everyone who seeks it, but only those chosen to fulfill a high calling')
    #Print Class Features
    print('For stat priority, Wisdom followed by Strength or Constitution.')
    
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
    print('-Armour:\n -Light armor, medium armor, shields')
    #Weapons: Simple weapons, martial weapons
    print('-Weapons:\n -Simple weapons')
    #Tools: None
    print('-Tools:\n -None')
    #Saving Throws: Strength, Constitution
    print('-Saving Throws:\n -Wisdom, Charisma')
    
    #Skills
    skills = ('History','Insight','Medicine','Persuasion','Religion')
    #fetching 2 unique strings from the tuple skills
    chosen_skills = random.sample(skills,2)
    print(f'Skills:\n -{chosen_skills}')
    
    #equipment
    print('\nEquipment')
    
    #weapons
    print('-Weapons')
    #first choice weapon
    first_choice = random.choice([1,2])
    if first_choice == 1:
        weapon,damage = Weapons.simple_melee_weapon('Mace')
    elif first_choice == 2:
        weapon,damage= Weapons.martial_melee_weapon('Warhammer')
    print(f'  Primary weapon{weapon,damage}')
    
    #second weapon choice 
    second_choice = random.choice(['Scale mail','Leather armor','Chain mail'])
    print(f'   Armour ({second_choice})')
    #Third choice
    Third_choice = random.choice([1,2])
    if Third_choice == 1:
        weapon, damage = Weapons.simple_ranged_weapon('Light Crossbow')
    elif Third_choice == 2:
        melee_or_range = random.choice(['melee','range'])
        if melee_or_range == 'melee':
            weapon,damage = Weapons.simple_melee_weapon()
        elif melee_or_range == 'range':
            weapon,damage = Weapons.simple_ranged_weapon()
    print(f'  Secondary weapon{weapon,damage}')
    #equipment pack
    print('-equipment pack')
    equipment_choice = random.choice([1,2])
    if equipment_choice == 1:
        equipment_pack = Equipment_packs.equipment_pack('Explorers_pack')
    elif equipment_choice == 2:
        equipment_pack = Equipment_packs.equipment_pack('Priests_kit')
    print(f'  {equipment_pack}')