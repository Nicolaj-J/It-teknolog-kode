from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
import _thread

class Servo3Stat:
    servomax = 90
    servomin = 35
    servonorm = 48
    hastighed = 100
    joystickmeasurement = 2048
    joystickmax = 2100
    joystickmin = 1700
    servooption = False

def Servo3():

    servo3=PWM(Pin(19),freq=50)
    servo3.duty(Servo3Stat.servonorm)
    check = Servo3Stat.servooption
    i = Servo3Stat.servonorm
    while(check == True):
        sleep_ms(int(Servo3Stat.hastighed))
        check = Servo3Stat.servooption
        y = int(Servo3Stat.joystickmeasurement)
        sleep(Servo1Stat.hastighed)
        if(int(y) <= int(Servo3Stat.joystickmin)):
            while(i > Servo3Stat.servomin and y <= Servo3Stat.joystickmin and check == True):
                check = Servo3Stat.servooption
                y = int(Servo3Stat.joystickmeasurement)
                servo3.duty(i)
                print(i)
                i = i - 1
                sleep_ms(Servo3Stat.hastighed)
        if(y >= int(Servo3Stat.joystickmax)):
            while(i < Servo3Stat.servomax and y >= Servo3Stat.joystickmax and check == True):
                check = Servo3Stat.servooption
                y = int(Servo3Stat.joystickmeasurement)
                print(i)
                servo3.duty(i)
                i = i + 1
                sleep_ms(Servo3Stat.hastighed)
