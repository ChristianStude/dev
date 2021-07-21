# 1: 5
# 2: 10
# 3: 15

#zahl = int(input("Bitte geben Sie eine Zahl zwischen 1 und 10 ein."))
for zahl in range(1, 11):
    print(f"{zahl:2d}:", end="")
    for faktor in range(1, 11):
        produkt = zahl * faktor
        print(f"{produkt:4d}", end="")
    print()
