import umqtt_robust2
import GPSfunk
from machine import Pin
from time import sleep_ms, sleep
import _thread
import micropyGPS
lib = umqtt_robust2
gps_status_n = 0
has_status_n = 0

def gps_status(status_gps):                         #Denne funktion som bliver startet som en tråd styre om devicet skal sende gps location eller ej
    global gps_status_n
    if status_gps == "start" and gps_status_n != 1: #Her ser funktionen på om den er blevet kaldt med en start kommando eller stop kommando samt om gps allerede sender data
        gps_status_n = 1                            #Sætter variablen til 1 som den en anden funktion kigger på
        _thread.start_new_thread(gps_loc, ())       #her starter den gps_loc funktionen i en tråd som opsender lokationen
        _thread.exit()                              #Her lukker den tråden
    elif status_gps == "stop" and gps_status_n != 0:#Funktionen ser på om den har fået stop kommandoen og om den allerede opsender locationen
        gps_status_n = 0                            #Beder den om at stoppe med at sende data
        _thread.exit()                              #lukker tråden

def hastighed_status(status_gps):                   #Denne funktion styre hvornår den opsender hastighedsmålinger.
    global has_status_n                             #Henter den globale variable til hastighed styring
    if status_gps == "start" and has_status_n != 1: #Kigger på om den er blevet bedt om at starte og om den allerede køre
        _thread.start_new_thread(hastighed, ())     #Her starter den tråden til hastighed opsending
        has_status_n = 1                            #ændre variablen til 1
    elif status_gps == "stop" and has_status_n != 0:#Kigger på om den er blevet bedt om at stoppe og om der er en tråd der køre
        has_status_n = 0                            #Sætter variablen til 0

def gps_loc():                                                              #Denne funktion som bliver alvet til en tråd styre gps lokation opsending
    while True:
        global gps_status_n                                                 #Henter den globale variable ned
        if gps_status_n == 1:                                               #Kigger på om den må opsende data. Denne variable bliver styret i gps_status() funktionen
            sleep(10)                                                       #Her bestemmer vi hvor hurtigt vi skal opsende data
            lib.c.publish(topic=lib.mqtt_gps_feedname, msg=GPSfunk.main())  #Poser gps lokation til cloud
        elif gps_status_n == 0:                                             #Hvis må poste data ser den på om den skal lukke tråden
            _thread.exit()                                                  #lukker tråden


def hastighed():                                                            #Denne funktion som bliver lavet til en tråd styre opsendingen af hastighed
    while True:
        global has_status_n                                                 #Henter den globale variable ned
        if has_status_n == 1:                                               #Kigger på om den må opsende hastighed
            speed = GPSfunk.main()                                          #Køre gpsfunk.main funktionen og får hastighed samt gps lokation i en retur
            speed = speed[:4]                                               #Splitter strengen vi får retur op. Det sker ved at vi tager de 5 første cifre og smider resten væk. Så ciffer 0,1,2,3,4. Disse cifre udgør hastigheden i strengen
            lib.c.publish(topic=lib.mqtt_kmt_feedname, msg=speed)           #poster hastigheden til cloud
            sleep(10)                                                       #sover i 10 sekunder
        elif has_status_n == 0:                                             #Ser på om tråden skal lukkes og opsending af data stoppes
            _thread.exit()                                                  #lukker tråden
