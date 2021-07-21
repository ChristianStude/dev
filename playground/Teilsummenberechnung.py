# Gegeben ist eine Zahl n >= 0
# Berechen die Summe s = 0 + 1 + 2 + ... + n-1 + n

while 1==1:
    zahl = int(input("Bitte geben Sie eine Zahl ein."))
    summe = 0

    for summand in range(0, zahl + 1):
        summe = summand + summe
        print("Teilsumme:", summe)

    print("Gesamtsumme:", summe)




