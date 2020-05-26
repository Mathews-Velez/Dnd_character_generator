import random 
import Class_files.Weapons as Weapons
import Class_files.Equipment_packs as Equipment_packs
def Barbarian(x):  
    
    #Print breif description
    print('\n\nYour class\n\nBarbarian\n -Filled with their destructive rage and primal instincts, the barbarian is the class you choose if you want to be the meat shield in the front line dealing great amounts of damage. Who needs a shield when you can stand your foes’ puny attacks with your hardened skin and/or high evasiveness?')
    #Print Class Features
    print('For stat priority, Strength followed by Constitution.')
    
    #Hit points
    #Hit Dice: 
    print('Hit Dice\n -d12')
    #Hit Points at 1st Level:modifier
    print('Hit points at Level 1\n 12 + Constitution_mod')
    #Hit Points at Higher Levels:
    print('Hit Points at Higher Levels: 1d12(or 7) + your constitution modifier per barbarian level after 1st')
     
    #Proficiencies
    print('\nProficiencies')
    #Armor: 
    print('-Armour:\n -Light armor, medium armor, shields')
    #Weapons: 
    print('-Weapons:\n -Simple weapons, martial weapons')
    #Tools:
    print('-Tools:\n -None')
    #Saving Throws:
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