import random
def Acolyte():
	print('\n\nYour Background\n\nAcolyte\n')
	Personality_Traits = ("I idolize a particular hero of my faith, and constantly refer to that person's dees and examples","I can find common ground between the fiercest enemies, empathizing with them and always working towards peace","I see omens in every event and action. The gods try to speak to us we just need to listen.","Nothing can shake my optimistic attitude.","I (mis)qutoe sacred texts and proverbs in almost every situation.","I am (in)tolerant of other faiths and (dis)respect the worship of other gods","I've enjoyed fine food, drink and high society among my temple's elite. Rough living grates on me","I've spent so long in the temple that I have little practical experiennce dealing with people in the outside world")
	Personality_Trait = random.choice(Personality_Traits)

	Ideals = ("TRADITION(Lawful): The ancient traditons of worship and sacrifice must be preserved and upheld","CHARITY(Good): I always try to help those in need.","CHANGE(Chaotic): We must help bring about the changes the gods are constantly working in the world","POWER(Lawful): I hope one day to rise to the top of my faith's religious hierarchy","FAITH(Lawful): I trust that may deity will guide my actions. I have faith that if I work hard, things will go well.","ASPIRATION(Any): I seek tp prove myself worthy of my god's favor by matching my actions against his or her teachings")
	Ideal = random.choice(Ideals)

	Bonds = ("I would die to recover an ancient relic of mmy faith that was lost a long time ago","I will someday get revenge on the corrupt temple hierarchy who branded me a heretic","I owe my life to the preist who took me in when my parents died.","Everything I do is for the common people.","I will do anything to protect the temple I served","I seek to preserve a sacred text that my enemies consider heretical and seek to destroy ")
	Bond = random.choice(Bonds)

	Flaws = ("I judge others harshly, and myself even more severely.","I put too much trust in those who weild power within my temple's hierarchy.","My piety sometimes leads me to trust those taht profess faith in my god","I am inflexible in my thinking.","I am suspicious of strangers and expect the worst of them.","Once I pick a goal, I become obsessed with it to the detriment of everything else in my life")
	Flaw = random.choice(Flaws)

	#Background Equipment

	print(f'Trait:\n -{Personality_Trait}')
	print(f'Ideal:\n -{Ideal}')
	print(f'Bond:\n -{Bond}')
	print(f'Flaw:\n -{Flaw}')
