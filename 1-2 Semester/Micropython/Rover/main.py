from machine import Pin,PWM


HøjreHbroStyring = Pin(4, Pin.OUT)
VenstreHbroStyring = Pin(14, Pin.OUT)

HøjreFrontHjulDirection = Pin(17, Pin.OUT)
HøjreBagHjulDirection = Pin(0, Pin.OUT)
VenstreFrontHjulDirection = Pin(27, Pin.OUT)
VenstreBagHjulDirection =Pin(13, Pin.OUT)

HøjreFrontHjulHastighed = PWM(Pin(16),freq=50)
HøjreBagHjulHastighed = PWM(Pin(15),freq=50)
VenstreFrontHjulHastighed = PWM(Pin(26),freq=50)
VenstreBagHjulHastighed  = PWM(Pin(12),freq=50)


def htest():
    HøjreHbroStyring.value(1)
    HøjreFrontHjulDirection.value(1)
    HøjreBagHjulDirection.value(0)
    HøjreFrontHjulHastighed.duty(500)
    HøjreBagHjulHastighed.duty(500)

def vtest():
    VenstreHbroStyring.value(1)
    VenstreFrontHjulDirection.value(1)
    VenstreBagHjulDirection.value(0)
    VenstreFrontHjulHastighed.duty(500)
    VenstreBagHjulHastighed.duty(500)
