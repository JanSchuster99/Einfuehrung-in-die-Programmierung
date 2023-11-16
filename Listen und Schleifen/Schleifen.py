desiredString = input("Bitte geben sie einen String ein: ")
quantity = -1
while quantity < 1:
    quantity = int(input("Bitte geben sie die Häufigkeit ein, muss Positiv sein: "))
i = 0
while i < quantity:
    print(desiredString)
    i += 1
else:
    print("###ENDE###")
