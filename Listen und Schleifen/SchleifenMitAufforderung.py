choice = "j"
while choice == "j":
    dividend = int(input("Geben sie den Dividend ein: "))
    divisor = int(input("Geben sie den Divisor ein: "))
    while(dividend >= divisor):
        dividend -= divisor
    print("Der rest beträgt " + str(dividend))
    choice = input("Wollen sie das Programm wiederholen? (j): ")
else:
    print("Programm beendet")