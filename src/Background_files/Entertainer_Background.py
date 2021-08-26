import random

def Entertainer():
	Entertainer_routines = ("Actor","Dancer","Fire-eater","Jester","Juggler","Instrumentalist","Poet","Singer","Storyteller","Tumbler","Gladiator")
	Entertainer_routine = random.choice(Entertainer_routines)

	Personality_traits = ("I know a story relevant to almost every situation.","Whenever I come to a new place, I collect local rumors and spread gossip.","I’m a hopeless romantic, always searching for that special someone.","Nobody stays angry at me or around me for long, since I can defuse any amount of tension.","I love a good insult, even one directed at me.","I get bitter if I’m not the center of attention.","I’ll settle for nothing less than perfection.","I change my mood or my mind as quickly as I change key in a song.")
	Personality_trait =random.choice(Personality_traits)

	Ideals = ("BEAUTY(Good) When I perform, I woulkd make the world better than it was","TRADITION(Lawful)The stories, legends, and songs of the past must never be forgotten, for they teach us who we are.","CREATIVITY(Chaotic) The world is in need of new ideas and bold actions.","GREED(Evil) I'm only in it for the money and fame. ","PEOPLE(Neutral)  I like seeing the smiles on people’s faces when I perform. That’s all that matters. ","HONESTY(Any) Art should reflect the soul; it should come from within and reveal who we really are.")
	Ideal =random.choice(Ideals)

	Bonds = ("My instrument is my most treasured possession, and it reminds me o f someone I love.", "Someone stole my precious instrument, and someday I’ll get it back.", "I want to be famous, whatever it takes.", "I idolize a hero o f the old tales and measure my deeds against that person’s.","I will do anything to prove myself superior to my hatedrival.","I would do anything for the other members of my old troupe.")
	Bond =random.choice(Bonds)

	Flaws = ("I’ll do anything to win fame and renown.","I’m a sucker for a pretty face.","A scandal prevents me from ever going home again.That kind of trouble seems to follow me around.","I once satirized a noble who still wants my head. It was a mistake that I will likely repeat.","I have trouble keeping my true feelings hidden. My sharp tongue lands me in trouble.","Despite my best efforts, I am unreliable to my friends.")
	Flaw =random.choice(Flaws)

	print('\n\nYour Background \n\nEntertainer\n')
	print('Skill proficiencies:\n -Acrobatics, Performance')
	print('Tool proficiencies:\n -Disguise kit, one type of musical instrument')
	print('Equipment:\n -A musical instrument (one of your choice),the favor of an admirer (love letter, lock of hair, or trinket), a costume, and a belt pouch containing 15 gp')
	print(f'Entertainer routine:\n -{Entertainer_routine}')
	print(f'Trait:\n -{Personality_trait}')
	print(f'Ideal:\n -{Ideal}')
	print(f'Bond:\n -{Bond}')
	print(f'Flaw:\n -{Flaw}')

def hello():
	print('Hello')
