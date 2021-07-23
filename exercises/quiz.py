import utils.tool
import random

fragenListe = utils.tool.LadeFragenliste("exercises\\fragen.json")
random.shuffle(fragenListe)

anzahlPunkte = 0

for aufgabe in fragenListe:
    print(aufgabe["frage"])
    utils.tool.gibAuswahloptionenAus(aufgabe["antworten"])
    eingabe = int(utils.tool.leseEingabe("Bitte gib eine der Antwortmöglichkeiten ein: ", ["1", "2", "3", "4"]))
    if eingabe == aufgabe["lösung"]:
        anzahlPunkte = anzahlPunkte + 1
        print("Das war Richtig!")

    else:
        print("Das war leider falsch.")

print("Du hast", anzahlPunkte, "Punkte erreicht!")


