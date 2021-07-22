import utils.tool
import random

fragenListe = utils.tool.LadeFragenliste("exercises\\fragen.json")
random.shuffle(fragenListe)

anzahlPunkte = 0

for aufgabe in fragenListe:
    print(aufgabe["frage"])
    utils.tool.gibAuswahloptionenAus(aufgabe["antworten"])
    eingabe = int(utils.tool.leseEingabe("Eingabe 1-4:", ["1", "2", "3", "4"]))
    if eingabe == aufgabe["lösung"]:
        anzahlPunkte = anzahlPunkte + 1
        print("Richtig!")
    else:
        print("Das war leider falsch.")

print("Du hast", anzahlPunkte, "erreicht!")


