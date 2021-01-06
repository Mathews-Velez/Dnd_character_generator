import random
def Charlatan():
	
	Favorite_schemes = ("I cheat at games of chance","I shave coins or forge documents","I insinuate myself into people's lives to prey on their weakness and secure their fortunes","I put on identities like clothes","I run sleight of hand cons on street corners.","I convince people that worthless junk is worth their hard earned money")
	Favorite_scheme = random.choice(Favorite_schemes)

	Personality_Traits = ("I fall in and out of love easily, and am always pursuing someone","I have a joke for every occasion, especially occasions where humor is inappropriate","Flattery is my preffered trick for getting what I want.","I'm a born gambler who can't resist taking a risk for a potential payoff.","I lie about almost everything, even when theres no good reason to","Sarcasm and insults are my weapon of choice.","I keep multiple holy symbols on me and invoke whatever deity might come in useful at any given moment.","I pocket anything I see that might have some value.")
	Personality_Trait = random.choice(Personality_Traits)

	Ideals = ("INDEPENDENCE(Chaotic): I am a free spirit-no one tells me what to do","FAIRNESS(Lawful): I never target people who can't afford to lose a few coins","CAHRITY(Good):I distribute the money I aquire to the people who really need it"," CREATIVITY(Chaotic): I never run the same con twice","FRIENDSHIP(Good): Material good come and go. Bonds of friendship last forever","ASPIRATION(Any): I'm determined to make something of myself")
	Ideal = random.choice(Ideals)

	Flaws = ("I can't resist a pretty face","I'm always in debt.I spend my ill-gotten gains on decadent luxuries faster than I bring them in.","I'm convinced that no one could ever fool me the way I fool others","I'm too greedy for my own good. I can't resist taking a risk if there's money involved.","I can't resist swindling people who are more powerful than me","I hate to admit it and will hate myself for it, but I'll run and perserve my own hide if the going gets tough. ")
	Flaw = random.choice(Flaws)

	
	print('\n\nYour Background \n\nCharlatan\n')
	print('Skill proficiencies:\n -Deception, Sleight of Hand')
	print('Tool proficiencies:\n -Disguise kit, forgery kit')
	print('Equipment:\n -A set o f fine clothes, a disguise kit, tools of the con of your choice (ten stoppered bottles filled with colored liquid, a set of weighted dice, a deck of marked cards, or a signet ring of an imaginary duke),and a belt pouch containing 15 gp')
	print(f'Scheme:\n -{Favorite_scheme}')
	print(f'Trait:\n -{Personality_Trait}')
	print(f'Ideal:\n -{Ideal}')
	print(f'Flaw:\n -{Flaw}')
