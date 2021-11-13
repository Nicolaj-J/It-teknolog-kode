import umqtt_robust2
import GPSfunk
from machine import Pin
from time import sleep_ms, sleep
import _thread
lib = umqtt_robust2
def gps_loc(gps_status):
    print(gps_status)
    while True:

        print(gps_status)
        if gps_status == "start":
            print("gps_loc kører")
            lib.c.publish(topic=lib.mqtt_gps_feedname, msg=GPSfunk.main())
            sleep(5)
        elif gps_status == "stop":
            print("gps_loc stoppet")
            break
            _thread.exit()

def hastighed():
    speed = GPSfunk.main()
    speed = speed[:4]
    print("speed: ",speed)
    lib.c.publish(topic=lib.mqtt_kmt_feedname, msg=speed)

