from hcsr04 import HCSR04
from time import sleep
from machine import Pin, ADC, PWM
import espnowsend
sensor= HCSR04(trigger_pin=25, echo_pin=26, echo_timeout_us=10000)


while(True):
    distance = sensor.distance_cm()
    if(distance < 5):
            espnowsend.SendData("buz")
    elif(distance > 5):
            espnowsend.SendData("stop")
