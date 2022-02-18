from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
import _thread
servo4=PWM(Pin(18),freq=50)
servo4max = 120
servo4min = 75
servo4norm = 70
i4 = servo4norm
x = 75
o = 0
def servo4checker():
    sleep(1)
def servo4styring():
    if(x < servo4max and o != 1):
        servo4.duty(x)
        x = x + 1
        if(x == servo4max):
            o = 1
    if(x > servo4min and o != 0):
        servo4.duty(x)
        x = x - 1
        if(x == servo4min):
            o = 0