from random import randint

def roll():
    return randint (1, 6)

choice = "j"
while choice == "j":
    print(roll())
    choice = input("Nochmal wuerfeln ? (j)")
else:
    print("Programm beendet")