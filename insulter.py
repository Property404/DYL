import random
def insult():
	prefixes = ["pig-slapping","cum-slurping","jimmy-jostling","anime-loving","garbage-eating",
	"puppy-fucking","creepy old","pedophilic","mountain-dew-drinking, dorito-eating","fedora-wearing"]
	
	nouns = ["cock monkey","grass eater","cod piece","buritto fucker","youtube commenter",
	"child licker","cake-sniffer","neckbeard","asscrack whore"]

	return random.choice(prefixes)+" "+random.choice(nouns)
