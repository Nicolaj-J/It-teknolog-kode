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
    servo4=PWM(Pin(19),freq=50)
    servo4.duty(Servo4Stat.servonorm)
    check = Servo4Stat.servooption
    while(check == True):
        check = Servo4Stat.servooption
        y = Servo4Stat.joystickmeasurement
        print("y1: ", y)
        sleep(1)
        if(y <= Servo4Stat.joystickmin):
            while(i >= Servo4Stat.servomin and y <= Servo4Stat.joystickmin and check == True):
                check = Servo4Stat.servooption
                y = Servo4Stat.joystickmeasurement
                servo2.duty(i)
                i = i - 1
                sleep_ms(Servo4Stat.hastighed)
        if(y >= Servo4Stat.joystickmax):
            while(Servo4Stat.servomax and y >= Servo4Stat.joystickmax and check == True):
                check = Servo4Stat.servooption
                y = Servo4Stat.joystickmeasurement
                servo4.duty(i)
                i = i + 1
                sleep_ms(Servo4Stat.hastighed)
