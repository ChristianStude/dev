# Lasse dir zwei Zahlen vom Benutzer geben und berechne das Produkt.
# Wenn das Produkt größer als 100, dann gib stattdessen die Summe der beiden Zahlen aus.
# print, input, if-anweisung

zahl1 = input("Gib bitte eine Zahl ein:")
zahl1 = int(zahl1)

zahl2 =input("Bitte gib eine weitere Zahl ein:")
zahl2 = int(zahl2)

produkt = zahl1 * zahl2
summe = zahl1 + zahl2

if produkt > 100:
    print("Die Summe der beiden Zahlen ist:", summe)
else: print ("Das Produkt der beiden Zahlen ist:", produkt)

print ("Vielen Dank für´s mitmachen")
