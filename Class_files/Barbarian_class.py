import random 
import Class_files.Weapons as Weapons
import Class_files.Equipment_packs as Equipment_packs
def Barbarian(x):  
    
    #Print breif description
    print('\n\nYour class\n\nBarbarian\n -A fierce warrior of primitive background who can enter a battle rage')
    #Print Class Features
    print('For stat priority, Strength followed by Constitution.')
    
    #Hit points
    #Hit Dice: 1d12 per barbarian level
    print('Hit Dice\n -d12')
    #Hit Points at 1st Level: 12 + your Constitution modifier
    print('Hit points at Level 1\n 12 + Constitution_mod')
    #Hit Points at Higher Levels: 1d12 (or 7) + your constitution modifier per barbarian level after 1st
    print('Hit Points at Higher Levels: 1d12(or 7) + your constitution modifier per barbarian level after 1st')
     
    #Proficiencies
    print('\nProficiencies')
    #Armor: Light armor, medium armor, shields
    print('-Armour:\n -Light armor, medium armor, shields')
    #Weapons: Simple weapons, martial weapons
    print('-Weapons:\n -Simple weapons, martial weapons')
    #Tools: None
    print('-Tools:\n -None')
    #Saving Throws: Strength, Constitution
    print('-Saving Throws:\n -Strength, Constitution')
    
    #Skills
    skills = ('Animal Handling','Athletics','Intimidation','Nature','Perception','Survival')
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
        weapon,damage = Weapons.martial_melee_weapon('Greataxe')
    else:
        weapon,damage= Weapons.martial_melee_weapon()
    print(f'  Primary weapon{weapon,damage}')
    #second weapon choice 
    second_choice = random.choice([1,3])
    if second_choice == 1:
        weapon, damage = Weapons.simple_melee_weapon('Handaxe')
    else:
        weapon, damage = Weapons.simple_melee_weapon()
    print(f'  Secondary weapon{weapon,damage}')
    #equipment pack
    print('-equipment pack')
    equipment_pack = Equipment_packs.equipment_pack('Explorers_pack')
    print(f'  {equipment_pack}')