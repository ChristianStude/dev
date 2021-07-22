import json

# Lasse den Nutzer solange eine Eingabe tätigen, bis die Eingabe einer der vorgegebenen Möglichkeiten entspricht.
def leseEingabe(prompt, eingabeOptionen):
    while True:
        eingabe = input(prompt)
        eingabe = eingabe.lower()
        if eingabe in eingabeOptionen:
            return eingabe

def gibAuswahloptionenAus(auswahlOptionen):
    print("Das sind die Auswahloptionen:")
    for index, option in enumerate(auswahlOptionen):
        print(index + 1, ": ", option, sep="")

def LadeFragenliste(pfad):
    fragenDatei = open(pfad, encoding="utf-8")
    fragenListe = json.load(fragenDatei)
    fragenDatei.close()
    return fragenListe
