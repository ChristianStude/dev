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


gibAuswahloptionenAus(["Stephan", "Mathias", "Christian", "Dyea", "Norbert"])
leseEingabe("Eingabe (1-5):", ["1", "2", "3", "4", "5"])

leseEingabe("Eingabe (A,B,C,D):", ["a", "b", "c", "d"])

leseEingabe("Eingabe: ja (j), nein (n), vielleicht (v):", ["j", "n", "v"])
