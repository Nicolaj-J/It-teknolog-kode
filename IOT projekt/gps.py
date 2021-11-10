import umqtt_robust2
import GPSfunk
from machine import Pin
from time import sleep_ms, sleep
lib = umqtt_robust2
x = 0
y = 0
a = 0
def gps_loc():
    print("gps_loc kører")
    lib.c.publish(topic=lib.mqtt_gps_feedname, msg=GPSfunk.main())


def hastighed():
    speed = GPSfunk.main()
    speed = speed[:4]
    print("speed: ",speed)
    lib.c.publish(topic=lib.mqtt_kmt_feedname, msg=speed)

