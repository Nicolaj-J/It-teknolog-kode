from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
import _thread

class Servo2Stat:
    servomax = 120
    servomin = 20
    servonorm = 70
    hastighed = 100
    joystickmeasurement = 2048
    joystickmax = 2100
    joystickmin = 1700
    servooption = False

def Servo2():

    servo2=PWM(Pin(22),freq=50)
    servo2.duty(Servo2Stat.servonorm)
    check = Servo2Stat.servooption
    i = Servo2Stat.servonorm
    while(check == True):
        sleep_ms(int(Servo2Stat.hastighed))
        check = Servo2Stat.servooption
        y = int(Servo2Stat.joystickmeasurement)
        sleep(Servo1Stat.hastighed)
        if(int(y) <= int(Servo2Stat.joystickmin)):
            while(i > Servo2Stat.servomin and y <= Servo2Stat.joystickmin and check == True):
                check = Servo2Stat.servooption
                y = int(Servo2Stat.joystickmeasurement)
                servo2.duty(i)
                i = i - 1
                sleep_ms(Servo2Stat.hastighed)
        if(y >= int(Servo2Stat.joystickmax)):
            while(i < Servo2Stat.servomax and y >= Servo2Stat.joystickmax and check == True):
                check = Servo2Stat.servooption
                y = int(Servo2Stat.joystickmeasurement)
                servo2.duty(i)
                i = i + 1
                sleep_ms(Servo2Stat.hastighed)
