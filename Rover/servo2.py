from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
import _thread
servo2=PWM(Pin(23),freq=50)
servo2max = 120
servo2min = 20
servo2norm = 70
i2 = servo2norm
x = 75
o = 0
def servo2checker():
    sleep(1)
def servo2styring():
    if(x < servo2max and o != 1):
        servo2.duty(x)
        x = x + 1
        if(x == servo2max):
            o = 1
    if(x > servo2min and o != 0):
        servo2.duty(x)
        x = x - 1
        if(x == servo2min):
            o = 0