import random
# background story
def Criminal():
	#Criminal speciality
	Criminal_specialities =("Blackmailer","Burglar","Enforcer","Fence","Highway robber","Hired killer","Pickpocket","Smuggler")
	Criminal_speciality = random.choice(Criminal_specialities)

	Personality_traits = ("I always have a plan for what to do when things go wrong.","I am always calm no matter the situation.I never raise my voice or let my emotions control me","The first thing I do in a new place is note the locations of everything valuable- or where such things could be hidden","I would rather make a new friend than make a new enemy","I am incredibly slow to trust.Those who seem the fairest often have the most to hide","I don't pay attention to the risks in a situation. Never tell me the odds","The best way to get me to do something is to tell me I can't do it","I blow up at the slightest insult")
	Personality_trait =random.choice(Personality_traits)

	Ideals = ("HONOR(Lawful):I don't steal from others in the trade","FREEDOM(Chaotic): Chains are meant to be broken as are those who would forge them","CHARITY(Good):I steal from the wealthy so I can give to those in need","GREED(Evil):I will do whatever it takes to become wealthy","PEOPLE(Neutral):I'm loyal to my friends, not to any ideals,and everyone else can take a trip down the Styx for all I care","REDEMPTION(Good):There's a spark of good in everyone")
	Ideal =random.choice(Ideals)

	Bonds = ("I'm trying to pay off an old debt I owe to a generous benefactor","My ill-gotten gains go to support my family","Something important was stolen from me, and I aim to steal it back","I will become the greatest theif that ever lived","I'm guilty of a terrible crime. I hope I can redeem myself for it.","Someone I loved died because of a mistake I made. That will never happen again")
	Bond =random.choice(Bonds)

	Flaws = ("When I see something valuable, I can't think about anything but how to steal it","When faced with a choice between money and my friends, I usually choose the money","If there's a plan , I'll forget it. If I don't forget it, I'll ignore it.","I have a 'tell' that reveals when I'm lying.","I turn tail and run when things look bad.","An innocent person is in prison for a crime that I committed.I'm okay with that.")
	Flaw =random.choice(Flaws)

	print('\n\nYour Background \n\nCriminal\n')
	print('Skill proficiencies:\n -Deception, Sleight of Hand')
	print('Tool proficiencies:\n -One type of gaming set, theives\' tools')
	print('Equipment:\n -A crowbar, a set of dark common clothes including a hood, and a belt pouch containing 15 gp.')
	print(f'Speciality:\n -{Criminal_speciality}')
	print(f'Trait:\n -{Personality_trait}')
	print(f'Ideal:\n -{Ideal}')
	print(f'Bond:\n -{Bond}')
	print(f'Flaw:\n -{Flaw}')
