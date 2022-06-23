import random
# background story
def background():
    #Defining Event
    Events = ("I stood up to a tyrant's agents.","I saved people during a natrul disaster.","I stood alone against a terrible monster.","I stole from a corrupt merchant to help the poor.","I led a militia to fight off an invading army.","I broke into a tyrant's castle and stole weapons to arm the people.","I trained the peasentry to use farm implements as weapons against a tyrant's soldiers.","A lord rescinded an unpopular decree after I led a symbolic act of protest against it.","A celestial, fey, or similar creature gave me a blessing or revealed my secret origin.","Recruited into a lord's army. I rose to leadership and was commended for my heroism.")
	#Personality trait
	Personality_traits = ("I judge people by their actuons, not their words.","If someone is in trouble, I'm always ready to help.","When I set my mind to something. I follow through no matter what gets in my way.","I have a strong sense of fair play and always try to find the most equitable solution to arguments.","I'm confident in my own abilities and do what I can to instill confidence in others.","Thinking is for other people. I prefer action.","I misuse long words in an attempt to sound smarter.","I get bored easily. When am I going to get on with my destiny?")
	Personality_trait =random.choice(Personality_traits)
	#Ideal
	Ideals = ("","","","","","","","")
	Ideals =random.choice(Ideals)
	#Bond
	Bonds = ("","","","","","","","")
	Bond =random.choice(Bonds)
	#Flaw
	Flaws = ("","","","","","","","")
	Flaw =random.choice(Flaws)
