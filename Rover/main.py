import afstand_beregning


command = ""
command = input()
if command == "start afstand":
    afstand_beregning.control_funktion_afstand(1)
    command = ""
elif command == "Stop afstand":
    afstand_beregning.control_funktion_afstand(0)
    command = ""

