# Zufallsgenerator
import random
random.seed()

# Werte und Berechnungen
a = random.randint(1, 10)
b = random.randint(1, 10)
c = a + b
print("Die Aufgabe lautet:", a, "+", b)

# Schleife uns Anzahl initialisieren
zahl = c + 1
versuch = 0

# Schleife mit while
while zahl != c:
    # Anzahl Versuche
    versuch = versuch + 1

    # Eingabe
    print("Bitte geben Sie eine Zahl ein!")
    z = input()
    
    # Versuch einer Umwandlung
    try:
        zahl = int(z)
    except:
        # Falls Umwandlung nicht erfolgreich
        print("Sie heben keine ganze Zahl eingegeben")
        # Schleife unmittelbar fortsetzen
        continue

    # Verzweigung
    if zahl == c:
        print(zahl, "ist richtig")
        # Abbruch der Schleife
        break
    else:
        print(zahl, "ist falsch")

# Anzahl ausgeben
print("Ergebnis: ", c)
print("Anzahl der Versuche: ", versuch)
