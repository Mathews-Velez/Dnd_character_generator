import random
#for simple melee weapons 
def simple_melee_weapon():
    #dictionary with weapon name attached with damage die and damage type
    simple_melee_weapons = {'Club': '1d4 bludgeoning ','Dagger':'1d4 piercing','Greatclub':'1d8 bludgeoning','Handaxe':'1d6 slashing','Javelin':'1d6 piercing','Light Hammer':'1d4 bludgeoning','Mace':'1d6 bludgeoning','Quarterstaff':'1d6 bludgeoning','Sickle':'1d4 slashing','Spear':'1d6 piercing'}
    weapon, damage  = random.choice(list(simple_melee_weapons.items()))
    return weapon,damage

#for simple ranged weapons 
def simple_ranged_weapon():
    #dictionary with weapon name attached with damage die and damage type
    simple_ranged_weapons = {'Light Crossbow':'1d8 piercing','Dart':'1d4 piercing','Shortbow':'1d6 piercing','Sling':'1d4 bludgeoning'}
    weapon, damage = random.choice(list(simple_ranged_weapons.items()))
    return weapon, damage

#for martial melee weapons 
def martial_melee_weapon():
    martial_melee_weapons = {'Battleaxe':'1d8 slashing','Flail':'1d8 bludgeoning','Glaive':'1d10 slashing','Greataxe':'1d12','Greatsword':'2d6','Halberd':'1d10 slashing','Lance':'1d12 piercing','Longsword':'1d8 slashing','Maul':'2d6 bludgeoning'}