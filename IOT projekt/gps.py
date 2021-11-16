import umqtt_robust2
import GPSfunk
from machine import Pin
from time import sleep_ms, sleep
import _thread
lib = umqtt_robust2
def gps_loc():
    while True:
        lib.c.publish(topic=lib.mqtt_gps_feedname, msg=GPSfunk.main())
        sleep(10)

def hastighed():
    while True:
        speed = GPSfunk.main()
        speed = speed[:4]
        print("speed: ",speed)
        lib.c.publish(topic=lib.mqtt_kmt_feedname, msg=speed)
        lib.c.publish(topic=lib.mqtt_debug_feedname, msg=str("kmt 1"))
        sleep(10)

