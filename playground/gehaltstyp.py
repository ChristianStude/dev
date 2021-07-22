# Lasse dir das Gehalt vom Nutzer eintippen!
# Wenn das Gehalt kleiner gleich  450,- €, dann gib MiniJobber aus, wenn kleiner gleich 1.000,- € ist
# dan gib Billiglohnarbeiter aus, wenn kleiner gleich 2.000,- € dann Normalverdiener ausgeben.
# Wenn das Gehalt größer als 8.000,- € dann Spitzennverdiener ausgeben.
while 1 == 1:
    gehalt = int(input("Bitte geben Sie die Höhe Ihres Geheltes ein!"))

    if gehalt <= 450:
        print("MiniJobber")
    elif gehalt <= 1_000:
        print("Billiglohnarbeiter")
    elif gehalt > 1_000 and gehalt <= 7_999:
        print("Normalverdiener")
    elif gehalt >= 8_000:
        print("Herzlichen Glückwunsch, Sie sind ein Spitzenverdiener.")
    else:
        print("keine Ahnung")
    input("Zum fortsetzen bitte die Enter-Taste drücken")
    
