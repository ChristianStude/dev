def printHello():
    print("Hallo, ich bin eine Funktion")
    print("Auf Wiedersehen.")

#printHello()

def berechneQuadrat(zahl):
    quadrat = zahl * zahl
    return quadrat

#print(berechneQuadrat(10))

def gehaltstyp():
        gehalt = int(input("Bitte geben Sie die Höhe Ihres Geheltes ein!"))

        if gehalt <= 450:
            return "MiniJobber"
        else:
            return "Normalverdiener"

#print(gehaltstyp())

def berechneQuersumme(zahl):
    quersumme = 0
    zeichen = str(zahl)
    for einZeichen in zeichen:
        ziffer = int(einZeichen)
        quersumme = quersumme + ziffer
    return quersumme

#print(berechneQuersumme(1234))

def berechneMaximum(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z
    elif x == y or x == z:
        return x
    elif y == x or y == z:
        return y
    elif z == x or z == y:
        return z

#print(berechneMaximum(5,5,5))

