def bruttoPreisRechner(nettopreis, zinssatz):
    return format(float(nettopreis*(zinssatz/100+1)), ".2f")

nettoPreis = float(input("bitte geben sie ihren Nettopreis ein: "))
zinssatz = float(input("bitte geben sie ihren Zinssatz ein: "))
print("Ihr Bruttopreis ist:", bruttoPreisRechner(nettoPreis, zinssatz), "€")