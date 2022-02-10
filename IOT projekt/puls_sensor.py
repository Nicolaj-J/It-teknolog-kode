# Write your code here :-)
from machine import Pin, ADC
from time import sleep_ms, sleep
import _thread
import umqtt_robust2
lib = umqtt_robust2
puls =  ADC(Pin(32))
puls.atten(ADC.ATTN_11DB)
puls_avg_list = []
puls_list = []
avg = 0
puls_BPM = 0
puls_n = 0

def puls_styring(puls_control):                     #Denne funktion styre hvornår puls sensoren skal køre.
    global puls_n                                   #Vi bruger denne globale variable til at kommunikere mellem denne funktion og de threads.
    if puls_control == "start" and puls_n != 1:     #Vi ser på om variablen vi har sendt til funktionen er start. Samtidig ser vi på om trådene allerede er bedt om at køre
        _thread.start_new_thread(puls_funktion, ()) #Funktionen starter en tråd til at måle puls og fordele målingerne
        _thread.start_new_thread(timer, ())         #Funktionen starter en funktion der bestemmer opsending af data samt convertering af adc værdi til BPM
        puls_n = 1                                  #Sætter den globale variable til 1
    elif puls_control == "stop" and puls_n != 0:    #Ser på om funktionen er blevet kaldt med en stop værdi samt om trådene køre.
        puls_n = 0                                  #Sætter den globale variable til 0 så trådene vil stoppe

def puls_funktion():                                                                    #Denne funktion som bliver lavet til en tråd tager puls målinger, laver et gennemsnit der giver en indikator om støjen samt fordæler målinger ud i lister
    while True:
        global puls_n
        global avg
        puls_val = puls.read()                                                          #laver en måling som giver en adc værdi
        sleep_ms(100)
        if puls_n == 1:                                                                 #ser på om den må køre
            if  len(puls_avg_list) < 10:                                                #kigger på om listen allerede har 10 målinger
                puls_avg_list.append(puls_val)                                          #hvis ikke ligger den målingen til listen
            elif len(puls_avg_list) >= 10:
                avg = sum(puls_avg_list) / len(puls_avg_list)                           #hvis listen har 10 eller over så laver den et gennemsnit af målingerne
                puls_avg_list.clear()                                                   #rydder listen
            if puls_val >= avg + 250:                                                   #ser om målingen er over gennemsnittet med en margin. Denne måling tæller vi som et hjerteslag
                puls_list.append(puls_val)                                              #placere målingen i en liste
        elif puls_n != 1:                                                               # hvis funktionen ikke må køre
            _thread.exit()                                                              # tråden lukker

def timer():                                                                            # Denne funktion som bliver lavet til en tråd styre konverteringen fra ADC til BPM samt upload til cloud af BPM
    while True:
        if puls_n == 1:                                                                 # Kigger på om tråden må køre
            sleep(10)                                                                   # Funktionen køre hvert 10 sekund for at få en BPM hvert 10 sekund
            global puls_BPM
            global puls_list
            puls_BPM = len(puls_list) * 6                                               #konvertere adc til BPM ved at kigge på hvor mange målinger vi har. Da en måling er et hjerteslag skal vi gange det op med 6.
            print(puls_BPM)
            if puls_BPM != 0:                                                           # Hvis BPM ikke er 0 uploader vi BPM til cloud
                lib.c.publish(topic=lib.mqtt_puls_feedname, msg=str(puls_BPM))
            else:
                pass
            puls_list.clear()                                                           #rydder listen med hjerteslag
        elif puls_n == 0:                                                               #hvis tråden ikke må køre lukker den
            _thread.exit()




