#Π17041-Python 3.6.4
import random
	
for k in range(0,1000):
	arithoimexribingo=0
	tries = 0
	players = []
	stoptheloop= False
	#δημιουργια λιστας παιχτων με 5 επιλογες για καθε εναν
	for i in range(0,100): 
		numbers = []
		for j in range(0,5): 
			x = random.randint(1,80)
			while x in numbers:
				x = random.randint(1,80)		
			numbers.append(x)
		players.append(numbers)

	Bingo = []
	#δημηιουργια λιστας αριθμων που αναγγελονται απο υπολογιστη 
	while stoptheloop == False:
		Bingo_number = random.randint(1,80)
		#χωρις επαναληψη
		while Bingo_number in Bingo:  
			Bingo_number = random.randint(1,80)
		#γεμισμα λιστας
		Bingo.append(Bingo_number)
       #οταν ο παιχτης βρισκει σωστο αριμο τοτε ο αριθμος στη players γινεται 0
		tries += 1
		for i in range(0,100):
			for j in range(0,5):
				if Bingo_number == players[i][j]:
					players[i][j] = 0



		for i in range(0,100):
			sum = 0
			for j in range(0,5):
				if players[i][j] == 0:
					sum += 1
			if sum == 5:
				stoptheloop = True

	arithoimexribingo += tries
average = arithoimexribingo/1000
print ("The average numbers that should be poped up in order to have bingo ", average)
