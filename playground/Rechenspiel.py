# Zufallsgenerator
import random
random.seed()

# Werte und Berechnungen
a = random.randint(1, 10)
b = random.randint(1, 10)
c = a + b
print("Die Aufgabe lautet:", a, "+", b)

# Schleife mit range
for versuch in range(1, 10):
    # Eingabe
    print("Bitte geben Sie eine Zahl ein!")
    z = input()
    zahl = int(z)

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
