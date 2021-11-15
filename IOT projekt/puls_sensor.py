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
def puls_funktion():
    while True:
        global n
        global avg
        puls_val = puls.read()
        sleep_ms(100)
        if  len(puls_avg_list) <= 10:
            puls_avg_list.append(puls_val)
        elif len(puls_avg_list) >= 10:
            avg = sum(puls_avg_list) / len(puls_avg_list)
            puls_avg_list.clear()
        if puls_val >= avg + 250:
            puls_list.append(puls_val)

def timer():
    while True:
        sleep(10)
        global puls_BPM
        global puls_list
        puls_BPM = len(puls_list) * 6
        print(puls_BPM)
        lib.c.publish(topic=lib.mqtt_puls_feedname, msg=str(puls_BPM))
        puls_list.clear()




