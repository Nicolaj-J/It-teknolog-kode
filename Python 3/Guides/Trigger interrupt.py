from machine import Pin
from time import sleep
led = Pin(26, Pin.OUT, value=0)
pir = Pin(27,Pin.IN)

def motion_detect(pir):
    print("Motion detected", pir.value())
    led.value(1)
    sleep(10)
    led.value(0)

pir.irq(trigger = Pin.IRQ_RISING, handler = motion_detect)
