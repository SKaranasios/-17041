#Π17041-Python 3.6.4
import random
import time

def bingo():   
    n=0
    #δημιουργια λιστων και αρχικοποιηση dictionary για αριθμο παιχτων και νουμερα παιχτων
    for z in range(1,1001):
        time.sleep(2)
        BingoNumbers=list(map(str,range(1,81)))
        randomchoice=list(map(str,range(1,81)))
        random.shuffle(randomchoice)
        players={}
        bingo={}
        #αρχικοποιηση σωστων επιλογων παιχτη και γεμισμα dictionary με αριθμο παιχτων 
        for i in range(1,101,1):
            bingo['{0}{1}'.format("player",i)]='0'
            PlayerNumbers=[]
            for j in range(0,5):
                PlayerNumbers.append(random.choice(randomchoice))
            players['{0}{1}'.format("player",i)]=PlayerNumbers
        #δημιουργια μεταβλητης για τεραμτισμο loop αν επιτευχθουν 5 σωστοι αριθμοι
        stoptheloop=False
        #επιλογη τυχαιου αριθμου απο λιστα
        for i in randomchoice:
            randomnumber=i
            n+=1
            #check για καθε παιχτη αν εχει το τυχαιο νουμερο στη λιστα του kαι προσθηκη του 1 στο string
            for j in range(1,101):
                if randomnumber in players['{0}{1}'.format("player",j)]:
                    bingo['{0}{1}'.format("player",j)]+=str(1)
                    if bingo['{0}{1}'.format("player",j)]=='011111':
                        stoptheloop= True
                        print("PLAYER "+str(j)+" WON")
                        break
            #εξοδος απο βροχο         
            if stoptheloop==True:
                break
            print(bingo)
    MO=n/1000
    print("Αverage of numbers to be announced in order to have bingo is  "+str(MO) )

bingo()
