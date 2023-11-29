
def shift(chosenString, key):
    shiftedString = ""
    for i in range(0, len(chosenString)):
        if chosenString[i].isalpha():
            shift = ord(key[i].upper()) - ord("A")
            if chosenString[i].isupper():
                letterIndex = ord(chosenString[i]) - ord("A")
                shiftedString = shiftedString + chr((letterIndex+shift)%26 + ord("A"))
            else:
                letterIndex = ord(chosenString[i]) - ord("a")
                shiftedString = shiftedString + chr((letterIndex+shift)%26 + ord("a"))
        else: 
            shiftedString = shiftedString + chosenString[i]
    return shiftedString

def adjustKey(chosenString, chosenKey):
    adjustedKey = ""
    for i in range(0, len(chosenString)):
        adjustedKey = adjustedKey + chosenKey[i%len(chosenKey)]
    return adjustedKey
choice = "y"
while choice == "y":
    chosenString = input("Geben sie ihren String ein: ")
    chosenKey = input("Geben sie den gewünschten Shift ein: ")
    adjustedKey = adjustKey(chosenString, chosenKey)
    shiftedString = shift(chosenString, adjustedKey)
    print("Verschlüsselter String: "+ shiftedString)
    choice = input("Nochmal? (y eingeben zum Wiederholen): ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
else:
    print("Programm geschlossen")  
