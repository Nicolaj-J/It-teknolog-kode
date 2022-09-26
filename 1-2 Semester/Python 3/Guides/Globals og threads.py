import _thread #importere bibloteket for at lave threads/tråde
import time
a = 0 #vi laver variablen som er den måde vi kommunikere med vores tråd

def tråd(): # det er denne funktion vi senere hen laver til en tråd
    while True:
        global a # kigger på om variablen a er har ændret sig for at bestemme hvilken vej i if/else den skal gå. Vi skal hente den globale variable før
                 # vi kan sende information ind i tråden ude fra
        if a == 0:
            print("tråden kører")
            time.sleep(2)
        else:
            print("tråden stoppet")
            _thread.exit() # her lukker vi tråden ned så den stopper med at køre

_thread.start_new_thread(tråd, ()) # her starter vi tråden op for første gang. Vi laver en tråd af funktionen ovenover
while True: # herinde køre styringen af åbningen og lukningen af tråde
    if a == 0: # inde i denne if lukker vi tråden ved at sætte a variablen til 1
        time.sleep(10)
        a = 1
    else: # nede i else starter vi tråden op igen ved at sætte variablen til 0(så tråden ikke lukker med det samme) samt starter en ny tråd op.
        time.sleep(0.5)
        print("starter tråden om 10 sekunder")
        time.sleep(10)
        a = 0
        _thread.start_new_thread(tråd, ())
