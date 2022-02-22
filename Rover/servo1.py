from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
import _thread

class Servo1Stat:
    servomax = 75
    servomin = 48
    servonorm = 48
    hastighed = 100
    joystickmeasurement = 2048
    joystickmax = 2100
    joystickmin = 1700
    servooption = 1

def Servo1():

    servo1=PWM(Pin(23),freq=50)
    servo1.duty(Servo1Stat.servonorm)
    check = Servo1Stat.servooption
    print(check)
    while(check == 1):
        sleep_ms(0.1)
        check = Servo1Stat.servooption
        print(Servo1Stat.joystickmeasurement)
        y = int(Servo1Stat.joystickmeasurement)
        print(y)
        sleep(1)
        if(int(y) <= int(Servo1Stat.joystickmin)):
            while(i >= Servo1Stat.servomin and y <= Servo1Stat.joystickmin and check == 1):
                check = Servo1Stat.servooption
                y = int(Servo1Stat.joystickmeasurement)
                print("servo 1,1")
                servo1.duty(i)
                i = i + 1
                sleep_ms(Servo1Stat.hastighed)
        if(y >= int(Servo1Stat.joystickmax)):
            while(Servo1Stat.servomax and y >= Servo1Stat.joystickmax and check == 1):
                check = Servo1Stat.servooption
                y = int(Servo1Stat.joystickmeasurement)
                print("servo 1,1")
                servo1.duty(i)
                i = i + 1
                sleep_ms(Servo1Stat.hastighed)
