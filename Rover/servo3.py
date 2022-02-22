from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
import _thread

class Servo3Stat:
    servomax = 75
    servomin = 48
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
    while(check == True):
        check = Servo3Stat.servooption
        y = Servo3Stat.joystickmeasurement
        sleep(1)
        if(y <= Servo3Stat.joystickmin):
            while(i >= Servo3Stat.servomin and y <= Servo3Stat.joystickmin and check == True):
                check = Servo3Stat.servooption
                y = Servo3Stat.joystickmeasurement
                servo3.duty(i)
                i = i - 1
                sleep_ms(Servo3Stat.hastighed)
        if(y >= Servo3Stat.joystickmax):
            while(Servo3Stat.servomax and y >= Servo3Stat.joystickmax and check == True):
                check = Servo3Stat.servooption
                y = Servo3Stat.joystickmeasurement
                servo3.duty(i)
                i = i + 1
                sleep_ms(Servo3Stat.hastighed)
