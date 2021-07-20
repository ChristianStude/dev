eingabe = input("Zeichenkette eingeben:")
print("Vierfache Eingabe in groß:", 4 * eingabe.upper())

if len(eingabe) >=2:
    print(eingabe[0], eingabe[1], eingabe[-2], eingabe[-1])
else: print("Bitte mehr als ein Zeichen eingeben!")
