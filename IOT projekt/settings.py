import umqtt_robust2
import time
lib = umqtt_robust2
besked = lib.besked
import _thread

def setting(device_number):
    lib.c.publish(topic=lib.mqtt_pub_feedname, msg= "Device %s ", device_number, " is connected")
    time.sleep(0.2)
    lib.c.publish(topic=lib.mqtt_pub_feedname, msg="Write settings to configure all connected devices or write settings followed by the device number")
    while True:
        if besked == "settings" or "settings ", + device_number:
            lib.besked = ""
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg="Entering settings on all devices")

