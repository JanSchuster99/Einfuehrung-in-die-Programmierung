#Nur für Demo!!
cyph = input("Bitte String eingeben: ")
for i in range(0, 26):
    decyph = ""
    for j in cyph:
        
        if j.isalpha():
            if j.isupper():
                decyph = decyph + chr((ord(j)-ord("A")+i)%26 + ord("A"))
            else:
                decyph = decyph + chr((ord(j)-ord("a")+i)%26 + ord("a"))
        else:
            decyph = decyph + j
    print(decyph)
