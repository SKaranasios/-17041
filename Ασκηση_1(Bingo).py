import random

n=0
for z in range(1,1001):

    BingoNumbers=list(map(str,range(1,81)))
    ls=list(map(str,range(1,81)))
    random.shuffle(ls)
    players={}
    succesfulguesses={}
    for i in range(1,101,1):
        succesfulguesses['{0}{1}'.format("player",i)]='0'
        PlayerNumbers=[]
        for j in range(0,5):
            PlayerNumbers.append(random.choice(ls))
        players['{0}{1}'.format("player",i)]=PlayerNumbers
    stoptheloop=False
    for i in ls:
        randomnumber=i
        n+=1
        for j in range(1,101):
            if randomnumber in players['{0}{1}'.format("player",j)]:
                succesfulguesses['{0}{1}'.format("player",j)]+=str(1)
                if succesfulguesses['{0}{1}'.format("player",j)]=='011111':
                    stoptheloop= True
                    print("PLAYER "+str(j)+" WON")
                    break
        if stoptheloop==True:
            break
        print(succesfulguesses)
MO=n/1000
print("O μέσος όρος του πόσοι αριθμοί πρέπει να αναγγελθούν ώστε να έχουμε Bingo σε 1000 παιχνιδια ειναι:"+str(MO) )
