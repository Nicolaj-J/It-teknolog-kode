from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
import _thread

class Servo4Stat:
    servomax = 75
    servomin = 48
    servonorm = 48
    hastighed = 100
    joystickmeasurement = 2048
    joystickmax = 2100
    joystickmin = 1700
    servooption = False

def Servo4():

    servo1=PWM(Pin(18),freq=50)
    servo1.duty(Servo4Stat.servonorm)
    check = Servo4Stat.servooption
    i = Servo4Stat.servonorm
    while(check == True):
        sleep_ms(int(100))
        check = Servo4Stat.servooption
        y = int(Servo4Stat.joystickmeasurement)
        sleep(1)
        if(int(y) <= int(Servo4Stat.joystickmin)):
            while(i > Servo4Stat.servomin and y <= Servo4Stat.joystickmin and check == True):
                check = Servo4Stat.servooption
                y = int(Servo4Stat.joystickmeasurement)
                servo1.duty(i)
                i = i - 1
                sleep_ms(Servo4Stat.hastighed)
        if(y >= int(Servo4Stat.joystickmax)):
            while(i < Servo4Stat.servomax and y >= Servo4Stat.joystickmax and check == True):
                check = Servo4Stat.servooption
                y = int(Servo4Stat.joystickmeasurement)
                servo1.duty(i)
                i = i + 1
                sleep_ms(Servo4Stat.hastighed)
