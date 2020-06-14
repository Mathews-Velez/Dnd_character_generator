from Class_files import Barbarian_class,\
	Bard_class,\
	Cleric_class,\
	Ranger_class,\
	Wizard_class,\
	Rogue_class,\
	Monk_class,\
	Druid_class,\
	Paladin_class,\
	Sorcerer_class,\
	Warlock_class,\
	Fighter_class

#Assign class strings in dictionary to class files
class_list = {
	'Barbarian': Barbarian_class.Barbarian,
	'Bard': Bard_class.Bard,
	'Cleric': Cleric_class.Cleric,
	'Fighter': Fighter_class.Fighter,
	'Ranger': Ranger_class.Ranger,
	'Wizard': Wizard_class.Wizard,
	'Rogue': Rogue_class.Rogue,
	'Monk': Monk_class.Monk,
	'Druid': Druid_class.Druid,
	'Paladin': Paladin_class.Paladin,
	'Sorcerer': Sorcerer_class.Sorcerer,
	'Warlock': Warlock_class.Warlock
}
