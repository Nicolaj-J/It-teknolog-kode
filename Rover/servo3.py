from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
import _thread
servo3=PWM(Pin(21),freq=50)
servo3max = 120
servo3min = 20
servo3norm = 70
i3 = servo3norm
x = 75
o = 0
def servo3checker():
    sleep(1)
def servo3styring():
    if(x < servo3max and o != 1):
        servo3.duty(x)
        x = x + 1
        if(x == servo3max):
            o = 1
    if(x > servo3min and o != 0):
        servo3.duty(x)
        x = x - 1
        if(x == servo3min):
            o = 0