from hcsr04 import HCSR04
from time import sleep
from machine import Pin, ADC, PWM
import _thread
# hc-sr05 pins for ESP32
sensor_højre = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)
sensor_venstre = HCSR04(trigger_pin=25, echo_pin=26, echo_timeout_us=10000)
x = 0
listeven = []
listehøj = []
listeavg = []
avgv = 0
avgh = 0
avg = 0
tid = 2
control_var = 0

def control_funktion_afstand(control):
    global control_var
    if control == 1 and control_var != 1:
        control_var = 1
        _thread.start_new_thread(afstand_højre, ())
        _thread.start_new_thread(afstand_venstre, ())
        _thread.start_new_thread(afstand_beregning, ())
    elif control == 0 and control_var != 0:
        control_var = 0

def tid_måling():
    global tid
    tid = input("Indtast tid imellem afstands måling i sekunder. Du skal bruge . istedet for ,")

def afstand_højre():
    global control_var
    while(control_var == 1):
        global avgh
        global tid
        distance_ven = sensor_højre.distance_cm()
        listeven.append(distance_ven)
        sleep(5)
        avgh = sum(listehøj)/len(listehøj)
        print("avgh: ", avgh)
        if len(listehøj) >= 10 :
            while(len(listehøj > 10)):
                listehøj.pop(0)

def afstand_venstre():
    global control_var
    while(control_var == 1):
        global avgv
        global tid
        distance_ven = sensor_venstre.distance_cm()
        listeven.append(distance_ven)
        sleep(5)
        avgv = sum(listeven)/len(listeven)
        print("avgv: ", avgv)
        if len(listeven) >= 10 :
            while(len(listeven > 10)):
                listehøj.pop(0)

def afstand_beregning():
    global control_var
    global listeavg
    while(control_var == 1):
        global avgv
        global avgh
        sleep(5)
        avg = avgv - avgh
        listeavg.append(avg)
        print("avg: ", avg)
        if len(listeavg) == 10:
            listeavg.pop(0)


