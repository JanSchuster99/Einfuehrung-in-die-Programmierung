import random
#OPTIONAL EIGENE ZAHLEN ANFANG
myNumbers = []
while len(myNumbers) < 6 :
    myNumber = 0
    while(myNumber < 1 or myNumber >49):  #Zahl muss zwischen 1 und 49 sein
      myNumber = int(input("Geben sie Zahl #" +str(len(myNumbers)+1)+ " ein: "))
    if myNumbers.count(myNumber) == 0: #Zahl darf nicht doppelt vorkommen
        myNumbers.append(myNumber)
ownSuperNumber = 0
while(ownSuperNumber < 1 or ownSuperNumber > 9):
    ownSuperNumber = int(input("Superzahl eingeben: "))
print("Ihre Lottozahlen sind:", myNumbers, "und ihre Superzahl ist:", ownSuperNumber)
#OPTIONAL EIGENE ZAHLEN ENDE

lotteryNumbers = []
while len(lotteryNumbers) < 6 :
    randomNumber = int(random.random()*49+1)
    if lotteryNumbers.count(randomNumber) == 0:
        lotteryNumbers.append(randomNumber)
superNumber = int(random.random()*9 + 1)
print("Die Lottozahlen sind:", lotteryNumbers, "und die Superzahl ist:", superNumber)

#OPTIONAL GEWONNEN ANFANG
myNumbers.sort()
lotteryNumbers.sort()
if myNumbers == lotteryNumbers:
    print("Ihre Lottozahlen stimmen überein")
else:
    print("Ihre Lottozahlen stimmen nicht überein")
if superNumber == ownSuperNumber:
    print("Ihre Superzahl stimmt überein")
else:
    print("Ihre Superzahl stimmen nicht überein")
#OPTIONAL GEWONNEN ENDE
