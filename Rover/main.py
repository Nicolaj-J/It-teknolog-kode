import afstand_beregning


command = ""
while(True):
    command = input()
    if command == "start afstand":
        afstand_beregning.control_funktion_afstand(1)
    elif command == "Stop afstand":
        afstand_beregning.control_funktion_afstand(0)

