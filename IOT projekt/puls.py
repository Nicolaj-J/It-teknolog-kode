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
        return temp, hum, tempf
    except:
        failed = "wasnt able to read sensor"
        return failed
