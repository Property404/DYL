import random
def insult():
	matrix = [[0 for x in range(5)] for x in range(5)] 
	matrix[0][0]="pig-slapping"
	matrix[0][1]="cum-slurping"
	matrix[0][2]="jimmy-jostling"
	matrix[0][3]="anime-loving"
	matrix[0][4]="garbage-eating"
	matrix[1][0]="cock monkey"
	matrix[1][1]="grass eater"
	matrix[1][2]="cod piece"
	matrix[1][3]="buritto fucker"
	matrix[1][4]="youtube commenter"
	prefix=random.randint(0,4)
	noun=random.randint(0,4)
	return ("you "+matrix[0][prefix]+ " " + matrix[1][noun]+".")
