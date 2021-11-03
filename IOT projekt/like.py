from machine import pin
import time
led_like = Pin(27, Pin.OUT, value=0)
like_counter = Pin(25, Pin.IN, value=0)
like_count = 0
def like():
    global like_count
    global like_counter
    global led_like
    try:
        for x in range (2):
            led_like = not led_like.value(led_like.value())
            time.sleep(0,5)
        like_count = like_count + 1
        like_counter = like_count
     except:
        failed = "Wasnt able to read sensor"
        lib.c.publish(tpic=lib.mqtt_pub_feedname, msg= failed)
        lib.besked = ""
def like_reset():
    global like_count
    global like_counter
    like_count = 0
    like_counter = like_count
