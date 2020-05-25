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
    martial_melee_weapons = {'Battleaxe':'1d8 slashing','Flail':'1d8 bludgeoning','Glaive':'1d10 slashing','Greataxe':'1d12 slashing','Greatsword':'2d6 slashing','Halberd':'1d10 slashing','Lance':'1d12 piercing','Longsword':'1d8 slashing','Maul':'2d6 bludgeoning', 'Morning star':'1d8 piercing', 'Pike':'1d10 piercing','Rapier':'1d8 piercing','Scimitar':'1d6 slashing','Shortsword':'1d6 piercing','Trident':'1d6 piercing','War pick ':'1d8 piercing','Warhammer':'1d8 bludgeoning','Whip':'1d4 slashing'}
    weapon, damage = random.choice(list(martial_melee_weapons.items()))
    return weapon, damage

#for martial ranged weapons
def martial_ranged_weapon():
    martial_ranged_weapons = {'Blowgun':'1 piercing','Crossbow, hand':'1d6 piercing','Crossbow, heavy':'1d10','Longbow':'1d8 piercing'}
    weapon, damage = random.choice(list(martial_ranged_weapons.itmes()))
    return weapon, damage