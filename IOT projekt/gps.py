import umqtt_robust2
import GPSfunk
from machine import Pin
from time import sleep_ms, sleep
lib = umqtt_robust2

def gps_loc(A):
    while True:
        if A == "start":
            print("gps_loc kører")
            lib.c.publish(topic=lib.mqtt_gps_feedname, msg=GPSfunk.main())
            sleep(5)
        elif A == "stop":
            break

def hastighed():
    speed = GPSfunk.main()
    speed = speed[:4]
    print("speed: ",speed)
    lib.c.publish(topic=lib.mqtt_kmt_feedname, msg=speed)

