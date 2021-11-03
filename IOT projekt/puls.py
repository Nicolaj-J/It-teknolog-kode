from machine import pin
import time
import dht
puls = dht.DHT11(Pin(14))
def puls():
    global puls
    try:
        puls.measure()
        temp = puls.temperature()
        hum = puls.humidity()
        tempf =  temp * (9/5) + 32.0
        lib.c.publish(tpic=lib.mqtt_puls_feedname, msg= puls)
        lib.besked = ""
    except:
        failed = "wasnt able to read sensor"
        lib.c.publish(tpic=lib.mqtt_pub_feedname, msg= failed)
        lib.besked = ""
