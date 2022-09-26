from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
import _thread

class Servo1Stat:
    servomax = 75
    servomin = 45
    servonorm = 50
    hastighed = 50
    joystickmeasurement = 2048
    joystickmax = 2100
    joystickmin = 1700
    servooption = False

def Servo1():

    servo1 = PWM(Pin(23),freq=50)
    servo1.duty(Servo1Stat.servonorm)
    check = Servo1Stat.servooption
    i = Servo1Stat.servonorm
    print("servo1 startet")
    while(True):
        sleep_ms(int(Servo1Stat.hastighed))
        check = Servo1Stat.servooption
        if(check == False):
            _thread.exit()
            break
        y = int(Servo1Stat.joystickmeasurement)
#         print("servo1 ", Servo1Stat.joystickmeasurement)
        if(int(y) <= int(Servo1Stat.joystickmin)):
            while(i > Servo1Stat.servomin and y <= Servo1Stat.joystickmin and check == True):
                check = Servo1Stat.servooption
                y = int(Servo1Stat.joystickmeasurement)
                servo1.duty(i)
                i = i - 1
                sleep_ms(Servo1Stat.hastighed)
        if(y >= int(Servo1Stat.joystickmax)):
            while(i < Servo1Stat.servomax and y >= Servo1Stat.joystickmax and check == True):
                check = Servo1Stat.servooption
                y = int(Servo1Stat.joystickmeasurement)
                servo1.duty(i)
                i = i + 1
                sleep_ms(Servo1Stat.hastighed)
    _thread.exit()
