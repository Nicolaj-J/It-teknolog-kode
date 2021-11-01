from machine import pin
import time
led_like = Pin(27, Pin.OUT, value=0)
like_count
def like():
    global like_count
    try:
        for x in range (2):
            led_like = not led_like.value(led_like.value())
            time.sleep(0,5)
        like_count = like_count + 1
        return like_count
     except:
        failed = "Wasnt able to read sensor"
        return failed
def like_reset():
    global like_count
    like_count = 0
    return like_count
