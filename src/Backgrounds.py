from dnd_character_generator.Background_files import Acolyte_Background,\
	 Charlatan_Background,\
	 Criminal_Background,\
	 Entertainer_Background

background_list = {
	'Acolyte': Acolyte_Background.Acolyte,
	'Charlatan': Charlatan_Background.Charlatan,
	'Criminal': Criminal_Background.Criminal,
	'Entertainer': Entertainer_Background.Entertainer,
}

background_skill_profinciencies = {
	'Acolyte': ['Insight','Religion'],
	'Charlatan':['Deception','Sleight of hand'],
	'Criminal':['Deception','Steallth'],
	'Entertainer':['Acrobatics','Performance'],
}


