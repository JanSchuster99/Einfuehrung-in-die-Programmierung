
def shift(chosenString, chosenShift):
    shiftedString = ""

    for i in range(0, len(chosenString)):
        if chosenString[i].isalpha():
            if chosenString[i].isupper():
                letterIndex = ord(chosenString[i])-ord("A")
                shiftedString = shiftedString + chr((letterIndex + chosenShift)% 26 + ord("A"))
            else:
                ord(chosenString[i])-ord("a") 
                shiftedString = shiftedString + chr((letterIndex + chosenShift) % 26 + ord("a"))
        else: 
            shiftedString = shiftedString + chosenString[i]
    return shiftedString

choice = "y"

while choice == "y":
    chosenString = input("Geben sie ihren String ein: ")
    chosenShift = int(input("Geben sie den gewünschten Shift ein: "))
    shiftedString = shift(chosenString, chosenShift)
    print("Verschlüsselter String: "+ shiftedString)
    choice = input("Nochmal? (y eingeben zum Wiederholen): ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
else:
    print("Programm geschlossen")  
