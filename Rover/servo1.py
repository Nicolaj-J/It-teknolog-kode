from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
import servostyring
import _thread
joy1x = ADC(Pin(33))
def servo1stat():
    servo1max = 120
    servo1min = 75
    servo1norm = 75
    i1 = servo1norm
    x = 75

status = 0
def servo1checker():
    return servostyring.servo1control("check")
def servo1styring():
    print("servostyring")
    status = 1
    o = 0
    servo1stat()
    # servo1=PWM(Pin(22),freq=50)
    while(status == 1):
        status == servo1checker()
        if(x < servo1max):
            print("ændre servo værdi", x)# servo1.duty(x)
            x = x + 1
            if(x == servo1max):
                o = 1
        if(x > servo1min ):
            print("ændre servo værdi", x) # servo1.duty(x)
            x = x - 1
            if(x == servo1min):
                o = 0
