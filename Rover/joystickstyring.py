from time import sleep, sleep_ms
from machine import Pin, PWM, ADC


def JoystickStyring(message):
    if(message == "check"):
        return joycontrol
    if(message == "servo"):
        joycontrol = True
    if(message == "motor"):
        joycontrol = False

def ReadjoyStickInput():
    sleep(1)
